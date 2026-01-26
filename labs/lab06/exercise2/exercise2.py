def match_specialists(candidates_list, project_requirements):
    skill_freq = {}
    for _, skills in candidates_list:
        for skill in skills:
            skill_freq[skill] = skill_freq.get(skill, 0) + 1

    rare_skills = {skill for skill, count in skill_freq.items() if count < 3}

    specialists = []
    for name, skills in candidates_list:
        
        if project_requirements.issubset(skills):
            
            candidate_rare_skills = skills & rare_skills
            if candidate_rare_skills:
                specialists.append((name, candidate_rare_skills))

    return specialists
