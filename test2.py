from lxml import etree
from collections import defaultdict
import pymongo

def insert_vulns(db, v_dict):
    bulk = db.vulns.initialize_unordered_bulk_op()
    for id, v in v_dict.items():
        bulk.find({'id':id}).upsert().update_one(
            { 
                '$set':{ 'v' : v },
                '$setOnInsert' : { 'id': id } 
            })

    bulk.execute()

def read_vulns(db, v_dict):
    d = {}
    for doc in db.vulns.find({ 
        'id' : 
        { 
            '$in' : list(v_dict) 
        } },
       {
           '_id':1,
           'id':1  
       }):
        d[doc['id']] = doc['_id']
        
    return d

def insert_nodes(db, n_dict):
    bulk = db.nodes.initialize_unordered_bulk_op()
    for ip, ids in n_dict.items():
        data = []
        for id in ids:
            data.append(id)
        bulk.find({ 'ip' : ip }).upsert().update_one(
            {
                '$addToSet' : { 'test_ids' : { '$each': data } },
                '$setOnInsert': 
                {
                    'ip' : ip                    
                }
            })
    
    bulk.execute()

def read_nodes(db, n_dict):
    d = {}
    for doc in db.nodes.find({ 
        'ip' : 
        { 
            '$in' : list(n_dict) 
        } },
       {
           '_id':1,
           'ip':1  
       }):
        d[doc['ip']] = doc['_id']
        
    return d

def set_node_vulns(db, nodes, v_ids):
    bulk = db.nodes.initialize_unordered_bulk_op()
    for ip, test_ids in nodes.items():
        data = []
        for t_id in test_ids:
            data.append(v_ids[t_id])
        bulk.find({'ip':ip}).update_one(
            { '$addToSet': { 'vulns' : { '$each': data } } })
    bulk.execute()

def set_vuln_nodes(db, vuln_nodes, n_ids):
    bulk = db.vulns.initialize_unordered_bulk_op()
    for v_id, ips in vuln_nodes.items():
        data = []
        for ip in ips:
            data.append(n_ids[ip])
        bulk.find({ 'id': v_id }).update_one(
            { '$addToSet': { 'nodes': { '$each' : data } } })
    bulk.execute()    

filename = "vuln.xml"
root = etree.parse(filename).getroot()
nodes = defaultdict(set)  # ip : [test1, test2...]
vulns = {}
for n in root.findall('.//node'):
    ip = n.attrib.get('ip')
    for t in n.findall('test'):
        nodes[ip].add(t.attrib.get('id'))
        
for v in root.findall('.//vulnerability'):
    vulns[v.attrib['id']] = v.attrib['v']

print('nodes', nodes)
print('vulns', vulns)

db = pymongo.MongoClient()['mytest']
insert_vulns(db, vulns)
insert_nodes(db, nodes)
v_ids = read_vulns(db, vulns)
n_ids = read_nodes(db, nodes)
set_node_vulns(db, nodes, v_ids)
vuln_nodes = defaultdict(set)
for ip, test_ids in nodes.items():
    for t_id in test_ids:
        vuln_nodes[t_id].add(ip)        
set_vuln_nodes(db, vuln_nodes, n_ids)
