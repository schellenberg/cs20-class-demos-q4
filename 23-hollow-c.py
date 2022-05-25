import turtle

canvas = turtle.Screen()
abde = turtle.Turtle()

#Schellenber's method
for side in [175, 25, 200, 200, 200, 25, 175, 0, 0, 150]:
    abde.forward(side)
    abde.left(90)

#cohen's method
# for side in [90, 10, 100, 100, 100, 10, 90]:
#     abde.forward(side)
#     abde.right(90)
# 
# abde.backward(80)


#ethan's method
# for thing in range(2):
#     abde.right(90)
#     abde.forward(20)
#     if thing == 0:
#         for other in range(3):
#             abde.right(90)
#             abde.forward(100)
# 
# abde.right(90)
# for thing in [80, 60, 80]:
#     abde.forward(thing)
#     abde.left(90)


#saabir's method
# for (length, turn) in [(60, 90), (120, 270), (20, 270), (100, 270), (80, 90), (100, 90), (20, 270), (120, 270), (60, 270)]:
#     abde.left(turn)
#     abde.forward(length)


#will's method
# for sides in range(3):
#     abde.backward(200)
#     abde.left(90)
# 
# abde.backward(20)
# 
# for sides in [180, 160, 180]:
#     abde.right(90)
#     abde.forward(sides)
#     
# abde.left(90)
# abde.forward(20)