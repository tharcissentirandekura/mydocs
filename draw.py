import picture
import sys

class Draw:
	def __init__(self,width,height):
		self.width = width	
		self.height = height

		picture.new_picture(self.width,self.height)
		
	def back_ground_color(self,color):
		self.color = color
		picture.set_fill_color(self.color)
		picture.draw_filled_rectangle(-1,-1,self.width,self.height)
		
	def shape(self,color):
		self.color = color
		picture.set_fill_color(self.color)
		picture.draw_filled_rectangle(0,0,self.width//2,self.height//3)
		
	def text(self,color,text,fontsize):
		self.text = text
		self.fontsize = fontsize
		self.color = color
		picture.set_outline_color(self.color)
		picture.draw_text(0,10,self.text,self.fontsize)


if __name__ == "__main__":
	draw = Draw(int(sys.argv[1]),int(sys.argv[1]))
	draw.back_ground_color("green")
	#draw.text("red","Tharcisse",10)
	draw.shape("orange")
	picture.draw_on_matrix()

