import re


def validate_answer(answer, sources):
    """
    Only validate numbers that are supposed to be cited.
    Ignore formatting noise.
    """

    # Extract number-citation pairs ONLY
    pairs = re.findall(r"(\d+\.?\d*)\s*\[(\d+)\]", answer)

    if not pairs:
        return {
            "status": "UNVERIFIED",
            "reason": "No valid cited numbers found"
        }

    source_map = {
        key.strip("[]"): value for key, value in sources.items()
    }

    for num, cite in pairs:
        if cite not in source_map:
            return {
                "status": "UNVERIFIED",
                "reason": f"Citation [{cite}] not found"
            }

        if num not in source_map[cite]:
            return {
                "status": "UNVERIFIED",
                "reason": f"{num} not found in source [{cite}]"
            }

    return {"status": "VERIFIED"}