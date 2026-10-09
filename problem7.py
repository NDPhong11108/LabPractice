def calculate_final_grade(s1, s2, s3):
    """Calculate the overall weighted grade.

    Args:
        s1 (float): assignment score (0-100), weighted 20%.
        s2 (float): midterm exam score (0-100), weighted 30%.
        s3 (float): final exam score (0-100), weighted 50%.

    Returns:
        float: the overall weighted score.
    """

    def weighted_score(score, weight):
        """Apply a weight to a score.

        Args:
            score (float): the score.
            weight (float): the weight as a decimal (e.g. 0.2 for 20%).

        Returns:
            float: score * weight.
        """
        return score * weight

    return weighted_score(s1, 0.2) + weighted_score(s2, 0.3) + weighted_score(s3, 0.5)


s1, s2, s3 = map(float, input().split())
print(f"Final Grade: {calculate_final_grade(s1, s2, s3):.2f}%")
