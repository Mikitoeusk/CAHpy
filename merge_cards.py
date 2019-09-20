from PIL import Image
import glob

#opens an image:
im = Image.open("D:/PyProjects/CAHpy/Back_Cards/black_back.png")
dir = "D:/PyProjects/CAHpy/Example_Cards/"
images = glob.iglob(dir + '*.png')
# for x in images:
#     print(x)

# print(im.size)
width = im.size[0]
height = im.size[1]

gap = 3
nwidth = width * 3 + 2 * gap
nheight = height * 4  + 3 * gap

page = 1
try:
    while images:
        new_page = Image.new('L', (nwidth , nheight), 255)
        for i in range(0, nwidth, width+gap):
            for j in range(0, nheight, height+gap):
                image = next(images)
                print(str(i) + "\t"+ str(j) + "\t" + image)
                card = Image.open(image)
                new_page.paste(card, (i,j))
                new_page.save("D:/PyProjects/CAHpy/Merged_Cards/Merged_page"+str(page)+".png")
        # new_page.show()
        print(f"Page {str(page)} saved")
        page += 1

except StopIteration:
    print(f"Page {str(page)} saved")
    print("finished")

# new_page = Image.new('L', (nwidth , nheight), 255)
# for i in range(0, nwidth, width+gap):
#     for j in range(0, nheight, height+gap):
#         new_page.paste(im, (i,j))
# new_page.save("D:/PyProjects/CAHpy/Merged_Cards/Merged_back_black.png")
