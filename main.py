#main 함수
import food_inputoutput as io
import food_find as find
import food_recipe as recipe

# main.py

def main():
    all_recipes = recipe.recipes()
    ingredients = io.get_user_ingredients()
    category = io.get_user_category_alternative()

    category_recipes = find.select_recipe_by_category(category, all_recipes)
    matched = find.filter_by_ingredients(category_recipes, ingredients)

    if not matched:
        print("입력한 재료로 만들 수 있는 요리가 없습니다.")
    else:
        io.show_recipe(matched[0])  # 점수 가장 높은 것만 보여줌

if __name__ == "__main__":
    main()

