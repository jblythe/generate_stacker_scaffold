from utility import generate_config
import yaml

instance1 = {
    "db_instance_identifier": "MyCoolInstance1"
}
instance2 = {
    "db_instance_identifier": "MyCoolInstance2"
}
instance3 = {
    "db_instance_identifier": "MyCoolInstance3"
}
instance4 = {
    "db_instance_identifier": "MyCoolInstance4"
}

reg_cluster1 = {
    "db_cluster_identifier": "MyCoolRegionalCluster1",
    "database_name": "myDataBase1",
    "instances": [instance1, instance2]
}
reg_cluster2 = {
    "db_cluster_identifier": "MyCoolRegionalCluster2",
    "database_name": "myDataBase1",
    "instances": [instance3, instance4]
}

glob_cluster_1 = {
    "global_cluster_identifier": "MyCoolGlobalCLuster",
    "source_db_cluster": "MyCoolRegionalCluster1",
    "clusters": [reg_cluster1]
}

glob_cluster_2 = {
    "global_cluster_identifier": "MyCoolGlobalCLuster",
    "source_db_cluster": "MyCoolRegionalCluster2",
    "clusters": [reg_cluster2]
}

config = generate_config([glob_cluster_1])

print(yaml.dump(config))

