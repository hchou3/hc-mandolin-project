import pdfplumber

def insurance_form_test():
    with pdfplumber.open("Input Data\Adbulla\PA.pdf") as pdf:
        first_page = pdf.pages[1]
        #print(pdf.metadata)
        #print(first_page.width, first_page.height)
        print("chars[0].text:", first_page.chars[0]['text'])

        extract_text = first_page.extract_text(x_tolerance=3, x_tolerance_ratio=None, y_tolerance=3, layout=False, x_density=7.25, y_density=13, line_dir_render=None, char_dir_render=None)
        print("extract_text:", extract_text)

def referral_form_test():
    with pdfplumber.open("Input Data/Adbulla/referral_package.pdf") as referral_pdf:
        im = referral_pdf.pages[0].to_image(resolution=150)
        print(im.extract_words())
if __name__ == "__main__":
    referral_form_test()