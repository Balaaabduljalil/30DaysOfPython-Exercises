#Level_one
import random
chars="abcdefghijklmnopqrstuvwxyz1234567890"
chars_list=[]
chars_list[:0]=chars
#quation_1
def random_user_id():
    identify=""
    for _ in range(6):
        identity += random.choice(chars_list)
        return identity
 #quation_2
def user_id_gen_by_user():
     for j in range(5):
         rand_colors=["#"+' '.join([random.choice("chars") for i in range(5)])]
         print(rand_colors)
#quation_3
def random_color():
    
     r = random.randint(0,255)
     g = random.randint(0,255)
     b = random.randint(0,255)
     rgb = [r,g,b]
     print('A Random color is :',rgb)
#Level_two   
#quation_1
def list_of_hexa_colors(many=0):
    if many==0:
        many=random.randint(1,10)
        hexas="1,2,3,4,5,6,7,8,9,0,a,b,c,d,e,f" .split(",")
        hexaCodes=[]
        for _ in range(many):
            hexaCodes.append("#" +' '. join([random.choice(hexas) for _ in range(6)]))
            return hexaCodes
 #quation_2           
def list_of_rgb_colors(many=0):
  if many==0:
      many=random.randint(1,10)
      rgbs=[]
      for _ in range(many):
          rgbs.append(rgb_color_gen())
          return rgbs
#quation_3
def generate_colors(type_of_color, many):
    if type_of_colors=="hexa":
        return list_of_hexa_colors(many)
    elif type_of_colors=="rgb":
        return list_of_rgb_colors(many)
    else:
        return "invalid input"
#level_3
#quation_1
def shuffled_list(array):
        return random.sample(array,len(array))
 #quation_2
def seven_random_numbers():
     arr =[]
     length = -1
     while length <=7:
         number=random.randint(0,9)
         if number not in arr:
             arr.append(number)
             length=len(arr)
             return arr
 
        
        
        