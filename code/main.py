# 모듈 임포트
import user_io as io          # 사용자 입력/출력 관련 함수들이 정의된 모듈
import food_finder as find    # 재료와 레시피 매칭 알고리즘이 들어있는 모듈
import food_recipe as recipe  # 전체 레시피 데이터 불러오기 함수가 정의된 모듈

# 프로그램의 진입점이 되는 main 함수 정의
def main():
    # 전체 레시피 데이터 불러오기
    all_recipes = recipe.load_recipes()

    # 사용자로부터 사용 가능한 재료 입력 받기 (예: 양파, 계란)
    ingredients = io.get_user_ingredients()

    # 사용자로부터 요리 카테고리 입력 받기 (예: 한식, 양식, 야식)
    category = io.get_user_category_alternative()

    # 선택한 카테고리에 해당하는 레시피들만 필터링
    category_recipes = find.select_recipe_by_category(category, all_recipes)

    # 사용자의 재료로 만들 수 있는 레시피 중 가장 적합한 것 찾기
    matched = find.filter_by_ingredients(category_recipes, ingredients)

    # 적합한 레시피가 없으면 안내 메시지 출력
    if not matched:
        io.show_no_result_message()
    else:
        # 가장 적합한 레시피를 출력 (점수 기준으로 최고점 1개만 선택됨)
        io.show_recipe(matched[0])

# 직접 실행될 경우 main 함수 실행
if __name__ == "__main__":
    main()
