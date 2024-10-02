food = [
    {'food': 'Spaghetti Aglio e Olio',
     'recipe': 'Cook spaghetti, sauté garlic in olive oil, add red pepper flakes, mix with pasta, and garnish with parsley.'
    },
    {'food': 'Chicken Adobo',
     'recipe': 'Marinate chicken in soy sauce, vinegar, garlic, and bay leaves, then simmer until cooked and sauce thickens.'
    },
    {'food': 'Caprese Salad',
     'recipe': 'Layer fresh mozzarella, tomatoes, and basil, drizzle with olive oil, and season with salt.'
    },
    {'food': 'Tacos',
     'recipe': 'Fill taco shells with seasoned ground beef, lettuce, cheese, and salsa; serve with lime wedges.'
    },
    {'food': 'Pancakes',
     'recipe': 'Mix flour, baking powder, sugar, milk, eggs, and butter; cook on a skillet until golden brown and serve with syrup.'
    },
    {'food': 'Fried Rice',
     'recipe': 'Sauté onions, carrots, and peas, add cooked rice and soy sauce, stir-fry until heated through; optionally add scrambled eggs.'
    },
    {'food': 'Vegetable Stir-Fry',
     'recipe': 'Sauté mixed vegetables in a wok with garlic and soy sauce; serve over rice or noodles.'
    },
    {'food': 'Chocolate Chip Cookies',
     'recipe': 'Cream butter and sugar, add eggs and vanilla, mix in flour and chocolate chips; bake until golden.'
    }
]

print (food)

print ('5th food recipe is: ', food[4]['recipe'])

food[2]['recipe'] = 'Layer fresh mozzarella, tomatoes, and basil, drizzle with olive oil and balsamic vinegar, and season with salt.'
print (food)

food.pop(6)

print ('Last food is: ', food[-1])