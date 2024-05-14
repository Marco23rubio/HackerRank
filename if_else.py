
# def run():
#     n = int(input())
#     if n >= 1 and n <=100:
#         if n % 2 ==0:
#             if n>=2 and n<=5 or n>20:
#                 print("Not Weird")
#             else:
#                 print("Weird")
#         else:
#             print("Weird")
#     else:
#         print("Agrega un numero menor a 100 y mayor a 1 (solo enteros)")

# if __name__ == "__main__":
#     run()

def is_leap(year):
    leap = False
    
    if year %4==0:
        if year %100==0:    
            if year %400 ==0:
                leap= False
            leap = True                
        leap = False        
    else:
        leap = False    
    return leap

year = int(input("algo: "))
print(is_leap(year))