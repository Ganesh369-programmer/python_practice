from pypdf import PdfWriter

# print(dir(PdfWriter))
merger = PdfWriter()

input1 = input("Enter the document name:- ")
input2 = input("Enter the document2 name:- ")

input3 = input("Enter the Mergin Document name:- ")

for pdf in [ input1 , input2]:
    merger.append(pdf)

merger.write(input3)
merger.close()

