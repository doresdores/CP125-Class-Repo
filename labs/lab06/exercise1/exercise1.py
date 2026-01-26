def get_legit_power_users(log_data, bot_ids, threshold):
    filter_bots = set()

    for timestamp, user_id, action_type in log_data:
       if user_id in bot_ids:
        continue
       
       if user_id not in bot_ids:
          filter_bots[user_id]=set()

    filter_bots[user_id].add(action_type)
    legit_power_users = set()
    
    for timestamp, user_id, actions in filter_bots.items():
        if timestamp >= threshold:
            legit_power_users.add(user_id)

    return legit_power_users
