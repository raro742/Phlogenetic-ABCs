import random
import pygame
from datetime import datetime

a_organisms=["Aardvark", "Albatross", "Alligator", "Alpaca", "Anaconda", "Ant", "Anteater", "Armadillo", "Axolotl", "Apple Tree"]
b_organisms= ["Baboon", "Badger", "Barnacle", "Barracuda", "Bat", "Bear", "Beaver", "Bee", "Beetle","Bison", "Boa Constrictor", "Bobcat", "Bonobo", "Butterfly"]
c_organisms=["Camel", "Capybara", "Cardinal", "Caribou", "Carp", "Cat", "Catfish", "Centipede", "Chameleon", "Cheetah", "Chicken", "Chimpanzee", "Chipmunk", "Clam", "Cobra", "Cockatoo", "Cockroach", "Cod", "Condor", "Coral", "Cougar", "Cow", "Coyote", "Crab", "Crane", "Cricket", "Crocodile", "Crow", "Cuckoo", "Carnation", "Cherry Tree", "Chrysanthemum", "Clover", "Crocus"]
list_of_2000_unique_abc_combinations=[]
list_of_first_3_of_2000_unique_abc_combinations=[]
list_of_first_3_a=[]
list_of_first_3_b=[]
list_of_first_3_c=[]
while len(list_of_first_3_a)<3:
    a=random.choice(a_organisms)
    if a not in list_of_first_3_a:
        list_of_first_3_a.append(a)
while len(list_of_first_3_b)<3:
    b=random.choice(b_organisms)
    if b not in list_of_first_3_b:
        list_of_first_3_b.append(b)
while len(list_of_first_3_c)<3:
    c=random.choice(c_organisms)
    if c not in list_of_first_3_c:
        list_of_first_3_c.append(c)
z=0
while z<3:
    abc_combination=[list_of_first_3_a[z], list_of_first_3_b[z], list_of_first_3_c[z]]
    list_of_2000_unique_abc_combinations.append(abc_combination)
    z+=1
list_of_2000_unique_abc_combinations.extend(list_of_first_3_of_2000_unique_abc_combinations)
while len(list_of_2000_unique_abc_combinations)<2000:
    a=random.choice(a_organisms)
    b=random.choice(b_organisms)
    c=random.choice(c_organisms)
    abc_combination=[a,b,c]
    if abc_combination not in list_of_2000_unique_abc_combinations and abc_combination[0] != list_of_2000_unique_abc_combinations[-1][0] and abc_combination[1] != list_of_2000_unique_abc_combinations[-1][1] and abc_combination[2] != list_of_2000_unique_abc_combinations[-1][2] and abc_combination[0] != list_of_2000_unique_abc_combinations[-2][0] and abc_combination[1] != list_of_2000_unique_abc_combinations[-2][1] and abc_combination[2] != list_of_2000_unique_abc_combinations[-2][2] and abc_combination[0] != list_of_2000_unique_abc_combinations[-3][0] and abc_combination[1] != list_of_2000_unique_abc_combinations[-3][1] and abc_combination[2] != list_of_2000_unique_abc_combinations[-3][2]:
        list_of_2000_unique_abc_combinations.append(abc_combination)
#print(list_of_2000_unique_abc_combinations)
#print(len(list_of_2000_unique_abc_combinations))


all_organisms = a_organisms + b_organisms + c_organisms
plant_list = ["Apple Tree", "Carnation", "Cherry Tree", "Chrysanthemum", "Clover", "Crocus"]
eudicots=["Apple Tree", "Carnation", "Cherry Tree", "Chrysanthemum", "Clover"]
monocots=["Crocus"]
rosids = ["Apple Tree", "Cherry Tree", "Clover"]
fabales=["Clover"]
rosales=["Apple Tree", "Cherry Tree"]
prunus=["Cherry Tree"]
malus=["Apple Tree"]
asterids_caryophyllales=["Carnation","Chrysanthemum"]
animal_list = [item for item in all_organisms if item not in plant_list]
mammals=["Aardvark", "Alpaca", "Anteater", "Armadillo", "Baboon", "Badger", "Bat", "Bear", "Beaver", "Bison", "Bobcat", "Bonobo", "Camel", "Capybara", "Caribou", "Cat", "Cheetah", "Chimpanzee", "Chipmunk", "Cougar", "Cow", "Coyote"]
pilosa_xenarthra_tubulidentata=["Anteater", "Armadillo", "Aardvark"]
primates=["Baboon", "Bonobo", "Chimpanzee"]
bonobo=["Bonobo"]
baboon=["Baboon"]
rodents=["Beaver", "Capybara", "Chipmunk"]
primates_rodents=primates+rodents
chiroptera=["Bat"]
carnivores=["Badger", "Bear", "Bobcat", "Cougar", "Coyote", "Cat", "Cheetah"]
cat_like_carnivores=["Bobcat", "Cougar", "Cat", "Cheetah"]
other_carnivores=["Badger","Bear","Coyote"]
cheetah_cougar=["Cheetah", "Cougar"]
cat=["Cat"]
even_toed_ungulates=["Alpaca", "Bison", "Camel", "Caribou", "Cow"]
cow_bison_caribou=["Cow", "Bison", "Caribou"]
cow_bison=["Cow", "Bison"]
caribou=["Caribou"]
alpaca_camel=["Alpaca", "Camel"]
carnivores_even_toed_ungulates=carnivores+even_toed_ungulates
carnivores_even_toed_ungulates_bats= carnivores_even_toed_ungulates+chiroptera
birds_and_reptiles=["Albatross", "Cardinal", "Chicken", "Cockatoo", "Condor", "Crane", "Crow","Cuckoo", "Alligator", "Crocodile","Chameleon","Anaconda", "Boa Constrictor", "Cobra"]
birds_and_crocodilia=["Albatross", "Cardinal", "Chicken", "Cockatoo", "Condor", "Crane", "Crow","Cuckoo", "Alligator", "Crocodile"]     
crocodilia=["Alligator", "Crocodile"]   
crocodiles=["Crocodile"]
alligators=["Alligator"]
birds=["Albatross", "Cardinal", "Chicken", "Cockatoo", "Condor", "Crane", "Crow","Cuckoo"]   
procelliformes=["Albatross"]
gruiformes=["Crane"]
cuculiformes=["Cuckoo"]
galliformes=["Chicken"]
passeriformes_psittaciformes_accipitrifores=["Cardinal", "Crow", "Cockatoo", "Condor"]
squamata=["Chameleon","Anaconda", "Boa Constrictor", "Cobra"]
lizards=["Chameleon"]
snakes=["Anaconda", "Boa Constrictor", "Cobra"]
anaconda_boa_constrictor=["Anaconda", "Boa Constrictor"]
cobra=["Cobra"]
amniotes=mammals+birds_and_reptiles
amphibians=["Axolotl"]
tetrapods=amniotes+amphibians
ray_finned_fish=["Barracuda", "Carp","Catfish","Cod"]
barracuda_cod=["Barracuda", "Cod"]
carp_catfish=["Carp","Catfish"]    
deuterostomes=mammals+birds_and_reptiles+squamata+amphibians+ray_finned_fish                                                                
protostomes=["Ant", "Barnacle", "Bee", "Beetle", "Butterfly", "Centipede", "Clam", "Cockroach", "Crab", "Cricket"]
bilateria=protostomes+deuterostomes
arthropods=["Ant", "Barnacle", "Bee", "Beetle", "Butterfly", "Centipede", "Cockroach", "Crab", "Cricket"]                                                  
insects=["Ant", "Bee", "Beetle", "Butterfly", "Cockroach", "Cricket"]
hymenoptera=["Ant", "Bee"]
formicidae=["Ant"]
anthophila=["Bee"]
lepidoptera=["Butterfly"]
coleoptera=["Beetle"]
blattodea=["Cockroach"]
orthoptera=["Cricket"]
lepidoptera_coleoptera=lepidoptera+coleoptera
lepidoptera_coleoptera_hymenoptera=lepidoptera_coleoptera+hymenoptera
blattodea_orthoptera=blattodea+orthoptera                                                        
crustaceans=["Barnacle", "Crab"]  
brachyurans=["Crab"]
cirripedians=["Barnacle"]
insects_crusaceans=insects+crustaceans                                                         
myriapoda=["Centipede"]
molluscs=["Clam"]
cnidiarians=["Coral"]

list_of_list_of_divergence_times=[]
#ab divergence times
for random_abc_list in list_of_2000_unique_abc_combinations:    
    list_of_divergence_times=[]
    if random_abc_list[0] in plant_list:
        ab_divergence_time=1500
    elif random_abc_list[0] in protostomes and random_abc_list[1] in deuterostomes or random_abc_list[0] in deuterostomes and random_abc_list[1] in protostomes:
        ab_divergence_time=800
    elif random_abc_list[1] in crustaceans and random_abc_list[0] in insects:
        ab_divergence_time=500
    elif random_abc_list[0] in hymenoptera and random_abc_list[1] in lepidoptera_coleoptera:
        ab_divergence_time=344
    elif random_abc_list[0] in formicidae and random_abc_list[1] in anthophila:
        ab_divergence_time=118
    elif random_abc_list[0] in tetrapods and random_abc_list[1] in ray_finned_fish:
        ab_divergence_time=450 
    elif random_abc_list[0] in amphibians and random_abc_list[1] in amniotes:
        ab_divergence_time=350
    elif random_abc_list[0] in mammals and random_abc_list[1] in birds_and_reptiles or random_abc_list[0] in birds_and_reptiles and random_abc_list[1] in mammals:
        ab_divergence_time=320
    elif random_abc_list[0] in birds_and_crocodilia and random_abc_list[1] in squamata or random_abc_list[0] in squamata and random_abc_list[1] in birds_and_crocodilia:
        ab_divergence_time=280
    elif random_abc_list[0] in anaconda_boa_constrictor and random_abc_list[1] in anaconda_boa_constrictor:
        ab_divergence_time=51
    elif random_abc_list[0] in pilosa_xenarthra_tubulidentata and random_abc_list[1] in mammals:
        ab_divergence_time=99
    elif random_abc_list[1] in primates_rodents and random_abc_list[0] in carnivores_even_toed_ungulates_bats:
        ab_divergence_time=94
    elif random_abc_list[0] in carnivores_even_toed_ungulates and random_abc_list[1] in chiroptera:
        ab_divergence_time=81
    elif random_abc_list[0] in even_toed_ungulates and random_abc_list[1] in carnivores:
        ab_divergence_time=76
    elif random_abc_list[1] in cow_bison_caribou and random_abc_list[0] in alpaca_camel:
        ab_divergence_time=64
    else:
        ab_divergence_time=2000
    list_of_divergence_times.append(ab_divergence_time)
#bc divergence times
    if random_abc_list[2] in plant_list:
        bc_divergence_time=1500
    elif random_abc_list[1] in bilateria and random_abc_list[2] in cnidiarians:
        bc_divergence_time=1000
    elif random_abc_list[2] in protostomes and random_abc_list[1] in deuterostomes or random_abc_list[2] in deuterostomes and random_abc_list[1] in protostomes:
        bc_divergence_time=800
    elif random_abc_list[2] in molluscs and random_abc_list[1] in arthropods:
        bc_divergence_time=600
    elif random_abc_list[2] in myriapoda and random_abc_list[1] in insects_crusaceans:
        bc_divergence_time=555
    elif random_abc_list[2] in crustaceans and random_abc_list[1] in insects or random_abc_list[2] in insects and random_abc_list[1] in crustaceans:
        bc_divergence_time=500
    elif random_abc_list[2] in brachyurans and random_abc_list[1] in cirripedians:
        bc_divergence_time=456
    elif random_abc_list[2] in blattodea_orthoptera and random_abc_list[1] in lepidoptera_coleoptera_hymenoptera:
        bc_divergence_time=383
    elif random_abc_list[2] in tetrapods and random_abc_list[1] in ray_finned_fish or random_abc_list[2] in ray_finned_fish and random_abc_list[1] in tetrapods:
        bc_divergence_time=450
    elif random_abc_list[2] in carp_catfish and random_abc_list[1] in barracuda_cod:
        bc_divergence_time=224
    elif random_abc_list[2] in barracuda_cod and random_abc_list[1] in barracuda_cod:
        bc_divergence_time=139
    elif random_abc_list[2] in mammals and random_abc_list[1] in birds_and_reptiles or random_abc_list[2] in birds_and_reptiles and random_abc_list[1] in mammals:
        bc_divergence_time=320
    elif random_abc_list[2] in birds_and_crocodilia and random_abc_list[1] in squamata or random_abc_list[2] in squamata and random_abc_list[1] in birds_and_crocodilia:
        bc_divergence_time=280
    elif random_abc_list[2] in cobra and random_abc_list[1] in anaconda_boa_constrictor:
        bc_divergence_time=86
    elif random_abc_list[2] in lizards and random_abc_list[1] in snakes:
        bc_divergence_time=161
    elif random_abc_list[2] in primates and random_abc_list[1] in rodents or random_abc_list[2] in rodents and random_abc_list[1] in primates:
        bc_divergence_time=87
    elif random_abc_list[2] in primates_rodents and random_abc_list[1] in carnivores_even_toed_ungulates_bats or random_abc_list[2] in carnivores_even_toed_ungulates_bats and random_abc_list[1] in primates_rodents:
        bc_divergence_time=94
    elif random_abc_list[2] in carnivores_even_toed_ungulates and random_abc_list[1] in chiroptera:
        bc_divergence_time=81
    elif random_abc_list[1] in even_toed_ungulates and random_abc_list[2] in carnivores or random_abc_list[1] in carnivores and random_abc_list[2] in even_toed_ungulates:
        bc_divergence_time=76
    elif random_abc_list[2] in primates and random_abc_list[1] in bonobo:
        bc_divergence_time=2
    elif random_abc_list[2] in primates and random_abc_list[1] in baboon:
        bc_divergence_time=29
    elif random_abc_list[2] in rodents and random_abc_list[1] in rodents:
        bc_divergence_time=70
    elif random_abc_list[1] in other_carnivores and random_abc_list[2] in other_carnivores:
        bc_divergence_time=45
    elif random_abc_list[1] in cat_like_carnivores and random_abc_list[2] in other_carnivores or random_abc_list[1] in other_carnivores and random_abc_list[2] in cat_like_carnivores:
        bc_divergence_time=55
    elif random_abc_list[1] in cat_like_carnivores and random_abc_list[2] in cheetah_cougar:
        bc_divergence_time=9
    elif random_abc_list[1] in cat_like_carnivores and random_abc_list[2] in cat:
        bc_divergence_time=12
    elif random_abc_list[1] in cow_bison and random_abc_list[2] in cow_bison:
        bc_divergence_time=4
    elif random_abc_list[2] in cow_bison_caribou and random_abc_list[1] in cow_bison:
        bc_divergence_time=23
    elif random_abc_list[1] in cow_bison_caribou and random_abc_list[2] in alpaca_camel:
        bc_divergence_time=64
    else:
        bc_divergence_time=3000
    list_of_divergence_times.append(bc_divergence_time)
#ac divergence times
    if random_abc_list[0] in plant_list and random_abc_list[2] in animal_list or random_abc_list[0] in animal_list and random_abc_list[2] in plant_list:
        ac_divergence_time=1500
    elif random_abc_list[0] in eudicots and random_abc_list[2] in monocots:
        ac_divergence_time=160
    elif random_abc_list[0] in rosids and random_abc_list[2] in asterids_caryophyllales:
        ac_divergence_time=118
    elif random_abc_list[0] in rosales and random_abc_list[2] in fabales:
        ac_divergence_time=96
    elif random_abc_list[0] in malus and random_abc_list[2] in prunus:
        ac_divergence_time=43
    elif random_abc_list[0] in bilateria and random_abc_list[2] in cnidiarians:
        ac_divergence_time=1000
    elif random_abc_list[0] in protostomes and random_abc_list[2] in deuterostomes or random_abc_list[0] in deuterostomes and random_abc_list[2] in protostomes:
        ac_divergence_time=800
    elif random_abc_list[2] in molluscs and random_abc_list[0] in arthropods:
        ac_divergence_time=600
    elif random_abc_list[2] in myriapoda and random_abc_list[0] in insects_crusaceans:
        ac_divergence_time=555
    elif random_abc_list[2] in crustaceans and random_abc_list[0] in insects:
        ac_divergence_time=500
    elif random_abc_list[2] in blattodea_orthoptera and random_abc_list[0] in lepidoptera_coleoptera_hymenoptera:
        ac_divergence_time=383
    elif random_abc_list[0] in tetrapods and random_abc_list[2] in ray_finned_fish:
        ac_divergence_time=450 
    elif random_abc_list[0] in amphibians and random_abc_list[2] in amniotes:
        ac_divergence_time=350
    elif random_abc_list[0] in mammals and random_abc_list[2] in birds_and_reptiles or random_abc_list[0] in birds_and_reptiles and random_abc_list[2] in mammals:
        ac_divergence_time=320
    elif random_abc_list[0] in birds_and_crocodilia and random_abc_list[2] in squamata or random_abc_list[0] in squamata and random_abc_list[2] in birds_and_crocodilia:
        ac_divergence_time=280
    elif random_abc_list[2] in crocodilia and random_abc_list[0] in crocodilia:
        ac_divergence_time=87
    elif random_abc_list[0] in birds_and_crocodilia and random_abc_list[2] in crocodilia or random_abc_list[0] in crocodilia and random_abc_list[2] in birds_and_crocodilia:
        ac_divergence_time=245
    elif random_abc_list[0] in procelliformes and random_abc_list[2] in gruiformes:
        ac_divergence_time=66
    elif random_abc_list[0] in procelliformes and random_abc_list[2] in passeriformes_psittaciformes_accipitrifores:
        ac_divergence_time=71
    elif random_abc_list[0] in procelliformes and random_abc_list[2] in cuculiformes:
        ac_divergence_time=74
    elif random_abc_list[0] in procelliformes and random_abc_list[2] in galliformes:
        ac_divergence_time=91
    elif random_abc_list[2] in cobra and random_abc_list[0] in anaconda_boa_constrictor:
        ac_divergence_time=86
    elif random_abc_list[2] in lizards and random_abc_list[0] in snakes:
        ac_divergence_time=161
    elif random_abc_list[0] in pilosa_xenarthra_tubulidentata and random_abc_list[2] in mammals:
        ac_divergence_time=99
    elif random_abc_list[2] in primates_rodents and random_abc_list[0] in carnivores_even_toed_ungulates_bats:
        ac_divergence_time=94
    elif random_abc_list[0] in even_toed_ungulates and random_abc_list[2] in carnivores:
        ac_divergence_time=76
    elif random_abc_list[2] in alpaca_camel and random_abc_list[0] in alpaca_camel:
        ac_divergence_time=21
    elif random_abc_list[2] in cow_bison_caribou and random_abc_list[0] in alpaca_camel:
        ac_divergence_time=64
    else:
        ac_divergence_time=3000
    list_of_divergence_times.append(ac_divergence_time)
    list_of_list_of_divergence_times.append(list_of_divergence_times)


pygame.init()
pygame.display.set_caption("ABC Phylogeny")
pygame.font.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
screen.fill((WHITE))  
pygame.draw.line(screen, (BLACK), (300, 400), (100, 125), 7)
pygame.draw.line(screen, (BLACK), (200, 262.5), (300, 125), 7)
pygame.draw.line(screen, (BLACK), (300, 400), (500, 125), 7)
pygame.draw.line(screen, (BLACK), (300, 400), (300, 460), 7)
pygame.draw.circle(screen, (BLACK), (300, 392), 13)
pygame.draw.circle(screen, (BLACK), (200, 254.5), 13)
p=0
game_font = pygame.font.SysFont("Arial", 24)
number_list_for_now=list_of_list_of_divergence_times[p]
species_list_for_now=list_of_2000_unique_abc_combinations[p]
largest_divergence_time=max(number_list_for_now)
smallest_divergence_time=min(number_list_for_now)
if smallest_divergence_time==number_list_for_now[0]:
    out_group=species_list_for_now[2]
    list_of_closest_organisms=[species_list_for_now[0], species_list_for_now[1]]
elif smallest_divergence_time==number_list_for_now[2]:
    out_group=species_list_for_now[1]
    list_of_closest_organisms=[species_list_for_now[0], species_list_for_now[2]]
else:
    out_group=species_list_for_now[0]
    list_of_closest_organisms=[species_list_for_now[1], species_list_for_now[2]]
random_list_of_closest_organisms=random.sample(list_of_closest_organisms, 2)
divergence_time_1=largest_divergence_time
divergence_time_2=smallest_divergence_time
text1 = game_font.render(f"{random_list_of_closest_organisms[0]}", True, (BLACK))
text2 = game_font.render(f"{random_list_of_closest_organisms[1]}", True, (BLACK))
text3 = game_font.render(f"{out_group}", True, (BLACK))
text4 = game_font.render(f"{divergence_time_1} mya", True, (BLACK))
text5 = game_font.render(f"{divergence_time_2} mya", True, (BLACK))
#text6=smaller_game_font.render("www.rachelrodman.com", True, (BLACK)) 
text_rect1 = text1.get_rect(center=(100,100))
text_rect2 = text2.get_rect(center=(300,100))
text_rect3 = text3.get_rect(center=(500,100))
screen.blit(text1, text_rect1)
screen.blit(text2, text_rect2)
screen.blit(text3, text_rect3)
screen.blit(text4, (330, 380))
screen.blit(text5, (230, 242.5))
#screen.blit(text6, (50,440))
#print(p)
MAKE_NEW_TREE = pygame.USEREVENT + 1
pygame.time.set_timer(MAKE_NEW_TREE, 6000, loops=2000)
clock = pygame.time.Clock()
pygame.display.flip() 

running = True
while running:
    clock = pygame.time.Clock()
    clock.tick(60)
    pygame.display.flip() 
    if p>1999:
        running=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    
        if event.type == MAKE_NEW_TREE:
            p+=1
            screen.fill((WHITE))  
            pygame.draw.line(screen, (BLACK), (300, 400), (100, 125), 7)
            pygame.draw.line(screen, (BLACK), (200, 262.5), (300, 125), 7)
            pygame.draw.line(screen, (BLACK), (300, 400), (500, 125), 7)
            pygame.draw.line(screen, (BLACK), (300, 400), (300, 460), 7)
            pygame.draw.circle(screen, (BLACK), (300, 392), 13)
            pygame.draw.circle(screen, (BLACK), (200, 254.5), 13)
            game_font = pygame.font.SysFont("Arial", 24)
            #smaller_game_font=pygame.font.SysFont("Arial", 11)
            number_list_for_now=list_of_list_of_divergence_times[p]
            species_list_for_now=list_of_2000_unique_abc_combinations[p]
            largest_divergence_time=max(number_list_for_now)
            smallest_divergence_time=min(number_list_for_now)
            if smallest_divergence_time==number_list_for_now[0]:
                out_group=species_list_for_now[2]
                list_of_closest_organisms=[species_list_for_now[0], species_list_for_now[1]]
            elif smallest_divergence_time==number_list_for_now[2]:
                out_group=species_list_for_now[1]
                list_of_closest_organisms=[species_list_for_now[0], species_list_for_now[2]]
            else:
                out_group=species_list_for_now[0]
                list_of_closest_organisms=[species_list_for_now[1], species_list_for_now[2]]
            random_list_of_closest_organisms=random.sample(list_of_closest_organisms, 2)
            divergence_time_1=largest_divergence_time
            divergence_time_2=smallest_divergence_time
            text1 = game_font.render(f"{random_list_of_closest_organisms[0]}", True, (BLACK))
            text2 = game_font.render(f"{random_list_of_closest_organisms[1]}", True, (BLACK))
            text3 = game_font.render(f"{out_group}", True, (BLACK))
            text4 = game_font.render(f"{divergence_time_1} mya", True, (BLACK))
            text5 = game_font.render(f"{divergence_time_2} mya", True, (BLACK))
            #text6=smaller_game_font.render("www.rachelrodman.com", True, (BLACK)) 
            text_rect1 = text1.get_rect(center=(100,100))
            text_rect2 = text2.get_rect(center=(300,100))
            text_rect3 = text3.get_rect(center=(500,100))
            screen.blit(text1, text_rect1)
            screen.blit(text2, text_rect2)
            screen.blit(text3, text_rect3)
            screen.blit(text4, (330, 380))
            screen.blit(text5, (230, 242.5))
            #screen.blit(text6, (50,440))
            #print(p)
            pygame.display.flip() 
       
        


