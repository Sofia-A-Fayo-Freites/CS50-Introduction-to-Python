from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.set_auto_page_break(auto=False)

    def title(self, title_text):
        self.set_y(20)
        page_width = self.w
        cell_width = 100
        x = (page_width - cell_width) / 2
        self.set_x(x)
        self.set_font("helvetica", "B", 40)
        self.cell(cell_width, 10, title_text, 0, new_x='LMARGIN', new_y='NEXT', align="C")

    def body(self):
        image_x, image_y = 30, 50
        image_w, image_h = 150, 160
        self.image("shirtificate.png", x=image_x, y=image_y, w=image_w, h=image_h)
        self.set_font("helvetica", "", 30)
        self.set_text_color(255,255,255)
        self.set_xy(image_x, image_y + (image_h / 2) - 30)
        self.cell(image_w, 10, f"{self.name} took CS50", 0, new_x='RIGHT', new_y='TOP', align="C")

def main():
    name = get_name()
    pdf = PDF(name)
    pdf.add_page()
    pdf.title("CS50 Shirtificate")
    pdf.body()
    pdf.output("shirtificate.pdf")

def get_name():
    name = input("Name: ")
    return name

if __name__ == "__main__":
    main()