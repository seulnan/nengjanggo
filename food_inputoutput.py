def get_user_ingredients():
    """
    사용자로부터 3가지 이상의 재료를 입력받아 리스트로 반환합니다.
    입력값의 앞뒤 공백을 제거하고 빈 값은 무시합니다.
    """
    while True:
        print("냉장고에 있는 재료를 3가지 이상 입력하세요. (쉼표로 구분):")
        user_input = input("예: 계란, 치즈, 밥\n> ")
        raw_ingredients = user_input.split(',')
        ingredients = []

        for item in raw_ingredients:
            temp_item = item
            # 앞쪽 공백 제거
            while len(temp_item) > 0 and temp_item[0] == ' ':
                temp_item = temp_item[1:]

            # 뒤쪽 공백 제거
            while len(temp_item) > 0 and temp_item[-1] == ' ':
                temp_item = temp_item[:-1]

            # 빈 문자열이 아니면 추가
            if len(temp_item) > 0:
                ingredients.append(temp_item)

        # 재료 개수 확인
        if len(ingredients) >= 3:
            return ingredients
        print("재료는 최소 3가지 이상 입력해야 합니다.\n")

def get_user_category_alternative():
    """
    사용자로부터 음식 카테고리(한식, 양식, 야식)를 입력받아 반환합니다.
    입력값의 앞뒤 공백을 제거하고 유효한 값인지 확인합니다.
    """
    while True:
        print("원하는 음식 카테고리를 선택하세요: 한식, 양식, 야식")
        user_input = input("> ")

        temp_category = user_input

        # 앞쪽 공백 제거
        while len(temp_category) > 0 and temp_category[0] == ' ':
            temp_category = temp_category[1:]

        # 뒤쪽 공백 제거
        while len(temp_category) > 0 and temp_category[-1] == ' ':
            temp_category = temp_category[:-1]

        category = temp_category

        # 유효한 카테고리인지 확인
        if category in ["한식", "양식", "야식"]:
            return category
        
        print("유효한 카테고리를 입력해주세요 (한식, 양식, 야식)\n")

def show_recipe(recommendation):
    """
    추천된 레시피 정보를 받아 형식에 맞게 출력합니다.
    """
    recipe = recommendation["recipe"]
    print(f"\n🥘 추천 요리: {recipe['name']}")
    print(f"📈 추천 점수: {recommendation['match_score']}%")

    # 전체 재료 출력 (for문 사용)
    ingredients_str = ""
    ingredient_list = recipe['ingredients']
    for i in range(len(ingredient_list)):
        ingredients_str += ingredient_list[i]
        if i < len(ingredient_list) - 1:
            ingredients_str += ", "
    print(f"📋 전체 재료: {ingredients_str}")

    # 현재 있는 재료 계산
    present = []
    for ingredient in recipe["ingredients"]:
        if ingredient not in recommendation["missing"]:
            present.append(ingredient)

    # 현재 있는 재료 출력 (for문 사용)
    present_str = ""
    for i in range(len(present)):
        present_str += present[i]
        if i < len(present) - 1:
            present_str += ", "
    print(f"✅ 현재 있는 재료: {present_str if present_str else '없음'}")

    # 부족한 재료 출력 (for문 사용)
    missing_str = ""
    missing_list = recommendation['missing']
    if len(missing_list) > 0:
        for i in range(len(missing_list)):
            missing_str += missing_list[i]
            if i < len(missing_list) - 1:
                missing_str += ", "
    else:
        missing_str = "없음"
    print(f"❌ 부족한 재료: {missing_str}")

    print(f"📖 레시피:\n{recipe['steps']}")
