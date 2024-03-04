from PIL import Image
image = Image.open('./pic/ai2.webp')
# image.load()
image.show()
image.save('./pic/ai2.png')
print('done')