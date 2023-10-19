import yaml

ENGINE_VERSION = 13.9
SRE_PRIVATE_SUBNETS = [
    "10.101.98.0/23",
    "10.102.98.0/23",
    "10.103.98.0/23",
    "10.104.98.0/23",
    "10.105.98.0/23",
    "10.106.98.0/23"
]


def create_instance(db_instance_identifier, allow_major_version_upgrade=True, allow_auto_minor_version_upgrade=True,
                    db_instance_class="db.r6g.large", enable_performance_insights=True,
                    performance_insights_retention_period=7, monitoring_interval=5, promotion_tier=0):
    instance = {
        "AllowMajorVersionUpgrade": allow_major_version_upgrade,
        "AllowAutoMinorVersionUpgrade": allow_auto_minor_version_upgrade,
        "DBInstanceClass": db_instance_class,
        "DBInstanceIdentifier": db_instance_identifier,
        "EnablePerformanceInsights": enable_performance_insights,
        "PerformanceInsightsRetentionPeriod": performance_insights_retention_period,
        "MonitoringInterval": monitoring_interval,
        "PromotionTier": promotion_tier
    }

    return instance


def create_regional_cluster(db_cluster_identifier, database_name, backup_retention_period=31, instances=[]):
    cluster = {
        "DBClusterIdentifier": db_cluster_identifier,
        "BackupRetentionPeriod": backup_retention_period,
        "DatabaseName": database_name,
        "MasterUsername": "adminUser",
        "Instances": []
    }

    for instance in instances:
        ins = create_instance(**instance)
        cluster['Instances'].append(ins)

    return cluster


def create_global_cluster(global_cluster_identifier, source_db_cluster, engine_version=ENGINE_VERSION,
                          sre_private_subnets=SRE_PRIVATE_SUBNETS, clusters=[]):
    g_cluster = {
        "GlobalClusterIdentifier": global_cluster_identifier,
        "EngineVersion": engine_version,
        "SREPrivateSubnets": sre_private_subnets,
        "SourceDBCluster": source_db_cluster,
        "Cluster": []
    }
    for cluster in clusters:
        r_cluster = create_regional_cluster(**cluster)
        g_cluster['Cluster'].append(r_cluster)

    return g_cluster


def generate_config(cluster_defs):
    global_clusters = {
        "vGlobalClusters": []
    }

    for cluster_def in cluster_defs:
        g_cluster = create_global_cluster(**cluster_def)
        global_clusters['vGlobalClusters'].append(g_cluster)

    return global_clusters
