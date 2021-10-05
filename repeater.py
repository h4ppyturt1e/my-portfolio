with open("copypaste.txt", "w") as f:
    f.write("<div class=\"column\">\n")
    for i in range(1, 44):
        if i % 11 == 0:
            f.write("</div>\n<div class=\"column\">\n")
        f.write(f"<img src=\"assets/{i}.jpg\" alt=\"Picture of Lato #{i}\">\n")
    f.write("</div>")