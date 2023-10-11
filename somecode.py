import re

a = '60b90c1c13067a15887e1ae1,Herbed Baked Salmon,4 lemons,1 large red onion,2 tablespoons chopped fresh basil\n', '60b90c2413067a15887e1ae2,Lemon Pancakes,2 tablespoons baking powder,1 cup vanilla-flavored almond milk,1 lemon\n', '60b90c2e13067a15887e1ae3,Chicken and Cold Noodles,6 ounces dry Chinese noodles,1 tablespoon sesame oil,3 tablespoons soy sauce\n', '60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese\n', '60b90c4613067a15887e1ae5,State Fair Lemonade,6 lemons,1 cups white sugar,5 cups cold water\n'

b = "60b90c1c13067a15887e1ae1"

re.search(b, a)