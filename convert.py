import img2pdf
name = input("image file name (example: photo.png):")
with open(name, "rb") as img:
    pdf_bytes = img2pdf.convert(img.read())
output = name.rsplit(".", 1)[0] + ".pdf"
with open(output, "wb") as f:
    f.write(pdf_bytes)
print("Done! Created", output)