def Role(s):
    if s<50:
        return "Manager"
    elif s>=90:
        return "Project Manager"
    elif s<70:
        return "Consultant"
    else:
        return "Lead Developer"
    
