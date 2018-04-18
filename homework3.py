import pandas as pd
import os


def create_dataframe(path="/class.db"):
    if not os.path.exists(os.getcwd() + path):
        raise ValueError

    statement = "SELECT video_id, category_id, 'ca' language FROM CAvideos GROUP BY video_id, category_id " + \
                "UNION ALL SELECT video_id, category_id, 'de' language FROM DEvideos GROUP BY video_id, category_id " + \
                "UNION ALL SELECT video_id, category_id, 'fr' language FROM FRvideos GROUP BY video_id, category_id " + \
                "UNION ALL SELECT video_id, category_id, 'gb' language FROM GBvideos GROUP BY video_id, category_id " + \
                "UNION ALL SELECT video_id, category_id, 'us' language FROM USvideos GROUP BY video_id, category_id;"

    return pd.read_sql(sql=statement, con="sqlite://" + path)
