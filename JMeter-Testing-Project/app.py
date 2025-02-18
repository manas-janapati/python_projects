from flask import Flask, request, jsonify, render_template
import matplotlib.pyplot as plt
import io
import base64
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/solve", methods=["POST"])
def solve():
    try:
        data = request.json
        option = data.get("option")
        results = []
        graphs = []

        if option == "hardcoded":
            # Hardcoded coefficients
            coefficients = [(1, -3, 2), (1, 2, 1)]
        elif option == "keyboard" or option == "single":
            # Single input or keyboard input
            coefficients = [(float(data["a"]), float(data["b"]), float(data["c"]))]
        elif option == "file":
            # File input (coefficients.txt in static folder)
            coefficients = []
            file_path = os.path.join("static", "coefficients.txt")
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    for line in file:
                        try:
                            a, b, c = map(float, line.strip().split())
                            coefficients.append((a, b, c))
                        except ValueError:
                            continue  # Skip invalid lines
            else:
                return jsonify({"error": "coefficients.txt not found in the static folder"}), 400
        elif option == "multiple":
            # Multiple inputs
            coefficients = []
            for input_set in data.get("inputs", []):
                if len(input_set) == 3:
                    try:
                        a, b, c = map(float, input_set)
                        coefficients.append((a, b, c))
                    except ValueError:
                        continue  # Skip invalid sets
        else:
            return jsonify({"error": "Invalid option"}), 400

        for index, (a, b, c) in enumerate(coefficients):
            if a == 0:
                results.append({
                    "description": f"Equation {index + 1}",
                    "roots": "Not a quadratic equation",
                    "a": a, "b": b, "c": c
                })
                continue

            discriminant = b ** 2 - 4 * a * c
            if discriminant > 0:
                root1 = (-b + discriminant ** 0.5) / (2 * a)
                root2 = (-b - discriminant ** 0.5) / (2 * a)
                roots = [root1, root2]
            elif discriminant == 0:
                root = -b / (2 * a)
                roots = [root]
            else:
                real_part = -b / (2 * a)
                imaginary_part = (abs(discriminant) ** 0.5) / (2 * a)
                roots = [f"{real_part} + {imaginary_part}i", f"{real_part} - {imaginary_part}i"]

            # Generate graph
            x = [i for i in range(-10, 11)]
            y = [a * (i ** 2) + b * i + c for i in x]
            plt.figure()
            plt.plot(x, y, label=f"{a}x² + {b}x + {c}")
            plt.axhline(0, color="black", linewidth=0.8)
            plt.axvline(0, color="black", linewidth=0.8)
            plt.title(f"Quadratic Equation {index + 1}")
            plt.legend()
            plt.grid(True)

            # Save graph as base64
            buf = io.BytesIO()
            plt.savefig(buf, format="png")
            buf.seek(0)
            graph_data = base64.b64encode(buf.read()).decode("utf-8")
            buf.close()
            graphs.append(graph_data)

            results.append({
                "description": f"Equation {index + 1}",
                "roots": roots,
                "a": a, "b": b, "c": c
            })

        return jsonify({"results": results, "graphs": graphs})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
