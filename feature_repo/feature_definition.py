"""
Defining metadata/feature that we want to store
"""
from datetime import timedelta

from feast import (
    Entity,
    FeatureView,
    Field,
    FileSource,
    ValueType
)
from feast.types import Int64

# ----------------Feature Data---------------- #
# Entity: the primary key
customer = Entity(
    name="customer",
    join_keys=["customer_id"],
    value_type=ValueType.INT64,
    description="ID of the customer"
)

# FileSource: object accepting path of the source file
feature_file_source = FileSource(
    path="data/features.parquet",
    event_timestamp_column="event_timestamp"
)


# FeatureView: grouping of features that are stored and managed together
features_data = FeatureView(
    name="features_data",
    # ttl: time to live, current setup equal to 1 day
    ttl=timedelta(seconds=86_400*1),
    entities=[customer],
    # schema: schema of the data that will be stored
    # on this case, the schema is following data that we used for modeling
    schema=[
        Field(name="customer_id", dtype=Int64),
        Field(name="salary", dtype=Int64),
        Field(name="age", dtype=Int64),
        Field(name="elevel", dtype=Int64),
        Field(name="car", dtype=Int64),
        Field(name="zipcode", dtype=Int64),
        Field(name="credit", dtype=Int64),
    ],
    # source: from where the data of the schema coming from
    # typically data warehouse
    source=feature_file_source,
    # online: True if online retrieval is enabled
    online=True,
    tags={}
)

# ----------------Target Data---------------- #
target_file_source = FileSource(
    path="data/target.parquet",
    event_timestamp_column="event_timestamp"
)

target_data = FeatureView(
    name="target_data",
    ttl=timedelta(seconds=86_400*1),
    entities=[customer],
    schema=[
        Field(name="customer_id", dtype=Int64),
        Field(name="brand", dtype=Int64)
    ],
    source=target_file_source,
    online=True,
    tags={}
)
