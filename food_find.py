import random

def filter_by_ingredients(recipes, user_ingredients):
    best_recipes = []  # 최고점수 레시피들 리스트
    best_score = -1

    for recipe in recipes:
        required = recipe["ingredients"]
        matched_count = 0
        missing = []

        for ingredient in required:
            if ingredient in user_ingredients:
                matched_count += 1
            else:
                missing.append(ingredient)

        score = matched_count / len(required)

        if score > 0:
            if score > best_score:
                best_score = score
                best_recipes = [{
                    "recipe": recipe,
                    "match_score": int(score * 100),  # 퍼센트로 반환
                    "missing": missing
                }]
            elif score == best_score:
                best_recipes.append({
                    "recipe": recipe,
                    "match_score": int(score * 100),
                    "missing": missing
                })

    if best_recipes:
        return [random.choice(best_recipes)]  # 최고점 중 하나 랜덤 선택
    else:
        return []

def select_recipe_by_category(category, all_recipes):
    for key in all_recipes:
        if key == category:
            return all_recipes[key]
    return []  # 유효하지 않은 경우 빈 리스트 반환
