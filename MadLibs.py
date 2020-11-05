######################################################################################################################################################################

# in this section we'll provide a choice between which story the user wants to adoperate

story_choice = input('What type of story would you like to be told \n'
                     '|| Sci-fi || Historical || Romantic || Horror ||\n')
story_choice = story_choice.lower()

# ask for user input
# diversity which text variable to be used based on the user selection



######################################################################################################################################################################
######################################################################################################################################################################


                ### part 1 ###
if story_choice == 'historical':
    city = input('insert a City name: \n')
    name = input('insert an actors name: \n')
    adjective = input('insert and adjective: \n')
    obj_first = input('insert a noun, something positive (plural): \n')
    franchise = input('insert a name of a famous franchise: \n')
    noun = input('insert a noun: \n')
    job_name = input('insert a Job name: \n')
    verb2 = input('insert a verb, something you consider weird (past tense): \n')
    verb3 = input('insert a verb, something you consider awesome (past tense): \n')
    obj_name = input('insert a Object name, something you would buy in a sex shop (plural): \n')
    noun2 = input('insert a noun, something you would expect in church: \n')
    name2 = input('insert the name of a family member: \n')
    noun3 = input('insert a noun, something cheeky (plural): \n')
    dessert = input('insert a dessert name (plural): \n')
    name3 = input('insert a celebrity name: \n')
    conspiracy = input('insert a conspiracy name: \n')
    spiritual_leader = input('insert the name of a spiritual leader: \n')
    tea = input('insert a noun, something you would use during tea time: \n')

    Historical_story = f'We were going up {city} with {name}——, asking the {adjective} walls, and the sidewalks ' \
                       f'torn up by {obj_first}, for the story of the siege of {franchise}, when, just before we reached ' \
                       f'the gigantic {noun}, the {job_name} {verb2} and, {verb3} one of the great {obj_name} so proudly grouped ' \
                       f'about the {noun2}, {name2} said to me:  “Do you see those four closed {noun3} up there on that balcony? ' \
                       f'In the early days of August, that terrible August of last year, so heavily laden with {dessert} and {name3}, ' \
                       f'I was called there to see a case of severe {conspiracy}-itis. \n' \
                       f'                                       -----------------------' \
                       f'It was the apartment of {name}, ' \
                       f'a {job_name} of {franchise}, an old enthusiast on the subject of {obj_name} and patriotism, ' \
                       f'who had come to live in {name3} with {spiritual_leader}, during the {conspiracy} outbreak. ' \
                       f'Guess why? In order to witness the triumphant return of our {job_name}. Poor old {noun}! The news of {noun3} ' \
                       f'reached him just as he was leaving the table. When he read the name of {obj_first} at the foot of that bulletin ' \
                       f'of defeat, he fell like a {tea}.  \n' \
                       f'                                       -----------------------' \
                       f'“I found the former cuirassier stretched out at full length on the carpet, ' \
                       f'his face covered with blood, andas lifeless as if he had received a blow on the head from a poleaxe. ' \
                       f'He must have been very tall when hewas standing; lying there, he looked enormous. Handsome features, ' \
                       f'magnificent teeth, a fleece of curlywhite hair, eighty years with the appearance of sixty. ' \
                       f'Beside him was his granddaughter, on her kneesand bathed in tears. She looked like him. ' \
                       f'One who saw them side by side might have taken them for twobeautiful Greek medallions, ' \
                       f'struck from the same die, one of which was old and earth-coloured, a littleroughened on the edges, ' \
                       f'the other resplendent and clean-cut, in all the brilliancy and smoothness of afresh impression.'
if story_choice == 'horror':
    adjective = input('insert and adjective: \n')
    profession = input('insert a profession (something you would never do): \n')
    noun = input('insert a body part noun: \n')
    verb = input('insert a verb (something you do when you\'re happy) : \n')



    Horror_story = f'He awoke to the {adjective}, {profession} like creatures looming over his {noun} and screamed his lungs out. ' \
                   f'They hastily left the room and he {verb} all night, {shaking} and {wondering} if it had been a dream.' \
                   f'The next morning, there was a {tap} on the door. Gathering his {courage}, he opened it to see one ' \
                   f'of them gently place a plate filled with fried {breakfast} on the floor, ' \
                   f'then retreat to a safe distance. Bewildered, he {accepted} the gift. The {profession} {chittered} excitedly.' \
                   f'This happened every day for weeks. At first he was worried they were {fattening} him up, but after ' \
                   f'a particularly greasy breakfast left him clutching his chest from heartburn, they were ' \
                   f'replaced with fresh {fruit}. ' \
                   f'                                       -----------------------' \
                   f'As well as cooking, they poured hot steamy {baths} for him and even ' \
                   f'tucked him in when he went to bed. It was {bizarre}. One night, he awoke to gunshots and {screaming}. ' \
                   f'He raced downstairs to find a decapitated {burglar} being devoured by the {profession}. He was {sickened}, ' \
                   f'but {disposed} the remains as best he could. He knew they had just been {protecting} him.' \
                   f'One morning the creatures wouldn\'t let him {leave} his room. He lay down, confused but trusting as ' \
                   f'they ushered him back into {bed}. Whatever their {motives}, they weren\'t going to hurt {him}.' \
                   f'Hours later a burning {pain} spread throughout his body. ' \
                   f'It felt like his stomach was filled with {razorwire}. The {profession} chittered as he spasmed and moaned. ' \
                   f'It was only when he felt a terrible squirming feeling beneath his {skin} that he ' \
                   f'realised the {profession} hadn\'t been protecting {him}. They had been protecting their {young}.'


                ### part 2 ###

# TO ADD
######################################################################################################################################################################
######################################################################################################################################################################

# use an if statement based on the user input
# if user chooses one story type print that text, else print another

if story_choice == 'historical':
       print(Historical_story)
if story_choice == 'horror':
       print(Horror_story)

######################################################################################################################################################################
######################################################################################################################################################################
