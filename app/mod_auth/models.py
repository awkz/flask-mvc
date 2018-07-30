# Import the database object from the main app module
from app import db,cur

def get_desa(id):
    cur.execute("select * from villages where id ='"+str(id)+"'")
    return cur.fetchone()

def insert_tiket():
    cur.execute("INSERT INTO `support_tiket` (`title`, `isi`, `iduser`, `status`, `created_time`, `update_time`) VALUES ('Test', 'Test aja', '1', 'closed', '2018-05-11 18:32:29', '2018-05-11 18:45:12');")
    db.commit()
    return "sukses"

def postx(**data):
    return data['pertama']+data['kedua']