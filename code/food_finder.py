import random

# 점수 계산 함수: 사용자가 가진 재료로 얼마나 레시피를 만들 수 있는지 점수를 계산
def calculate_match_score(required, user_ingredients):
    matched_count = 0  # 사용자가 가지고 있는 재료 수
    missing = []       # 사용자가 가지고 있지 않은 재료 목록

    # 모든 필요 재료를 순회하여 개별적으로 확인
    for ingredient in required:
        # 사용자가 보유한 재료라면 matched 개수 증가
        if ingredient in user_ingredients:
            matched_count += 1
        # 사용자가 보유하지않은거라면 누락리스트에 추가
        else:
            missing.append(ingredient)

    score = matched_count / len(required)  # 전체 재료 중 몇 개를 가지고 있는지 비율 계산
    return score, missing  # 점수와 누락된 재료를 함께 반환

# 사용자의 재료를 기준으로 레시피들을 필터링하여 가장 적합한 것 하나를 선택
def filter_by_ingredients(recipes, user_ingredients):
    best_recipes = []  # 최고 점수의 레시피들을 담을 리스트
    best_score = -1    # 비교를 위한 초기 점수값

    # 모든 레시피에 대해 재료 일치율을 평가
    for recipe in recipes:
        required = recipe["ingredients"]  # 해당 레시피의 재료 목록만 추출
        score, missing = calculate_match_score(required, user_ingredients)  # 점수 계산

        if score > 0:  # 적어도 하나의 재료가 맞는 경우만 고려 (score=0인 완전 불일치인 레시피제외)
            if score > best_score:
                best_score = score # 최고점수 갱신
                best_recipes = [{ # 기존 후보는 삭제하고 현재 레시피만 저장
                    "recipe": recipe,
                    "match_score": int(score * 100),  # 점수를 0~100 범위로 표현
                    "missing": missing
                }]
            elif score == best_score:
                # 점수가 같으면 리스트에 추가하여 나중에 랜덤 선택 가능하게
                best_recipes.append({
                    "recipe": recipe,
                    "match_score": int(score * 100),
                    "missing": missing
                })

    if best_recipes:
        return [random.choice(best_recipes)]  # 최고 점수 중 하나를 무작위로 선택하여 반환
    else:
        return []  # 어떤 레시피도 조건에 맞지 않으면 빈 리스트 반환

# 사용자가 선택한 음식 카테고리에 해당하는 레시피 리스트 반환
def select_recipe_by_category(category, all_recipes):

    # 딕셔너리의 모든 키(카테고리 이름)를 순회
    for key in all_recipes:
        # 사용자가 선택한 카테고리와 일치하는지 확인
        if key == category:
            return all_recipes[key]  # 일치하는 카테고리의 레시피들 반환
    return []  # 반목문 끝날때까지 못찾으면 (유효하지 않은 카테고리이면) 빈 리스트 반환
