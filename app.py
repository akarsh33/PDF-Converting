from flask import Flask, request, send_file
import img2pdf
import io
app = Flask(__name__)
@app.route("/")
def home():
    return """
    <style>
        body{
            
            font-family: Arial, sans-serif;
                text-align: center;
                background-color: lightblue;
                margin-top: 80px;
                
            }
        button{
            background-color: green;
            color:white;
            padding: 10px,24px;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
              }
       .card{
            background-color: white;
            width: 400px;
            margin:0 auto;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 2px 10px lightgray;
            }

    </style>
    <div class="card">
    <h1>PDF Converter</h1>
    <p> Choose an image to convert to PDF: </p>
    <form action="/convert" method="post" enctype="multipart/form-data">
    <input type="file" name="image" accept="image/*" multiple>
    <button type="submit">Convert</button>
    </form>
    </div>
    """
@app.route("/convert", methods=["POST"])
def convert():
    files = request.files.getlist("image")

    if len(files) == 0 or files[0].filename == "":
        return "Please choose an image first. <a href='/'>Go back</a>"
    try:
        pdf_bytes = img2pdf.convert([f.read() for f in files])
    except Exception:
        return "Sorry, that file is not a valid image.<a href='/'>Go Back</a>"
    if len(files) == 1:
        name = files[0].filename.rsplit(".",1)[0] + ".pdf"
    else:
        name = "combined.pdf"
    return send_file(
        io.BytesIO(pdf_bytes),
        mimetype="application/pdf",
        as_attachment=True,
        download_name=name,
)
app.run(debug=True)
 