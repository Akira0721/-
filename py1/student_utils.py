
def parse_student(line):
    line = line.strip()
    if not line:
        return None
    parts = line.split(",")
    if len(parts)!=2:
        raise ValueError(f"字段数量错误，行内容:{line}")
    name, score_str = parts
    name = name.strip()
    score_str = score_str.strip()
    if len(name)==0:
        raise ValueError("姓名为空")
    try:
        score = int(score_str)
    except ValueError:
        raise ValueError(f"成绩不是整数:{score_str}")
    if not (0 <= score <=100):
        raise ValueError(f"成绩越界0~100:{score}")
    return {"name":name, "score":score}
