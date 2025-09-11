# from pypdf import PdfReader

# reader = PdfReader("codingquestion6_9.pdf")
# number_of_pages = len(reader.pages)
# print(number_of_pages)
# for page in reader.pages:
#     text = page.extract_text()
#     print(text)


from pypdf import PdfWriter

merger = PdfWriter()


input1 = open("nearloop.pdf", "rb")
input2 = open("codingquestion6_9.pdf", "rb")
input3 = open("doc.pdf", "rb")

# Append entire input3 document to the end of the output document
merger.append(input1)

# Append entire input3 document to the end of the output document
merger.append(input2)

# Append entire input3 document to the end of the output document
merger.append(input3)

# Write to an output PDF document
output = open("document-output.pdf", "wb")
merger.write(output)

# Close file descriptors
merger.close()
output.close()