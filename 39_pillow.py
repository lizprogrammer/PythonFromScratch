from PIL import Image

i = Image.open('bunny.jpg')
i.show()


#i.rotate(45).show()
#i.rotate(45).save('bunny.png')
j = Image.open('hammy.jpg')
#j.show()

#i.convert('LA').show()
print(i.format)
print(i.size)
print(i.height)
print(i.width)
i.crop((0,0,400,300)).show()