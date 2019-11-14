# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 11:45:47 2019

@author: kjaglicic
"""

# Airflow, setting up DAG

import airflow
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
import timedelta


# Setting up default arguments for DAG initialization
default_args = {
        'owner': 'airflow',
        'start_date' : airflow.utils.dates.days_ago(2)
        }


# Initializing our DAG
dag = DAG(
        dag_id = 'DAG_tmp',
        default_args = default_args,
        description = 'DAG for DSC, temporary',
        schedule_interval = timedelta(days=1)
        )


# Defining Tasks
##############

# Reading data

read_data_1 = DummyOperator(
        task_id = 'Read data',
        dag=dag
        )

read_data_2 = DummyOperator(
        task_id = 'Read data',
        dag=dag
        )

read_data_3 = DummyOperator(
        task_id = 'Read data',
        dag=dag
        )

read_data_4 = DummyOperator(
        task_id = 'Read data',
        dag=dag
        )

read_data_5 = DummyOperator(
        task_id = 'Read data',
        dag=dag
        )

read_data_6 = DummyOperator(
        task_id = 'Read data',
        dag=dag
        )

read_data_7 = DummyOperator(
        task_id = 'Read data',
        dag=dag
        )

read_data_8 = DummyOperator(
        task_id = 'Read data',
        dag=dag
        )

# Models

task_churn_model = DummyOperator(
        task_id='Churn prediction model creation',
        dag=dag
        )

task_seq_events = DummyOperator(
        task_id='Sequence of impacting events',
        dag=dag
        )

task_content_ctg = DummyOperator(
        task_id='Content Categorization',
        dag=dag
        )

task_competitor_call_rec = DummyOperator(
        task_id='Competitor calls recognition',
        dag=dag
        )

task_cei = DummyOperator(
        task_id='CEI – Experience Index',
        dag=dag
        )

task_sna = DummyOperator(
        task_id='Social Network Analytics (SNA)',
        dag=dag
        )

task_beh_clust = DummyOperator(
        task_id='Behavior clusters',
        dag=dag
        )

task_offer_optimization = DummyOperator(
        task_id='Offer optimization',
        dag=dag
        )

# Making scoring table

making_scoring_table = DummyOperator(
        task_id='Making scoring table',
        dag=dag
        )


# Setting up dependecies in our workflow

[read_data_1>>task_churn_model, read_data_2>>task_seq_events, read_data_3>>task_content_ctg,\
 read_data_4>>task_competitor_call_rec,read_data_5>>task_cei, read_data_6>>task_sna,\
 read_data_7>>task_beh_clust, read_data_8>>task_offer_optimization] >> making_scoring_table











