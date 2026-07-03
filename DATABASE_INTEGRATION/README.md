# Database Integration – Digital Nurture 5.0

> **Author:** **RUCHITRA T**
> **Module:** Database Integration
> **Program:** Digital Nurture 5.0 – Python Full Stack Engineer (Python FSE) Deep Skilling

---

# Overview

This repository contains the practical exercises completed as part of the **Database Integration** module of the **Digital Nurture 5.0 – Python Full Stack Engineer (Python FSE) Deep Skilling Program**.

The module provides hands-on experience in relational and NoSQL database development using **MySQL**, **MongoDB**, **SQLAlchemy ORM**, and **Alembic**. The exercises gradually progress from database design and SQL programming to ORM implementation, query optimization, schema migrations, and database version control.

---

# Repository Structure

```text
Database Integration/
├── HandsOn-1/          # Database Design & Normalization
├── HandsOn-2/          # SQL Data Manipulation
├── HandsOn-3/          # Advanced SQL Programming
├── HandsOn-4/          # Query Optimization & Performance
├── HandsOn-5/          # MongoDB Database Operations
├── HandsOn-6/          # SQLAlchemy ORM
├── HandsOn-7/          # Alembic Database Migrations
└── DatabaseIntegration_HandsOn.pdf
```

---

# Project Scenario

All practical exercises are based on a **College Management System** database named **college_db**.

The database consists of the following entities:

| Table           | Purpose                                             |
| --------------- | --------------------------------------------------- |
| **departments** | Stores department information and allocated budgets |
| **students**    | Maintains student records linked to departments     |
| **courses**     | Contains course information offered by departments  |
| **enrollments** | Records student enrollment details and grades       |
| **professors**  | Stores faculty information including salary details |

---

# Hands-On Exercises

## HandsOn-1 – Database Design and Normalization

**Technology:** MySQL

This exercise focuses on creating a relational database from scratch while applying normalization principles to eliminate redundancy and improve data consistency.

### Files

| File                                   | Description                      |
| -------------------------------------- | -------------------------------- |
| `TablesInput.sql`                      | Reference schema                 |
| `Task1_Create_Database_and_Tables.sql` | Database and table creation      |
| `Task2_Normalization_Analysis.txt`     | Analysis of normalization levels |
| `Task3_Alter_Table.sql`                | Table modification operations    |

### Concepts Covered

* Database creation
* Table creation
* Primary and Foreign Keys
* Normalization (1NF, 2NF, 3NF)
* ALTER TABLE operations
* CHECK constraints

---

## HandsOn-2 – SQL Data Manipulation

**Technology:** MySQL

Introduces Data Manipulation Language (DML) statements and SQL queries used for managing and retrieving information from relational databases.

### Files

| File                             | Description                          |
| -------------------------------- | ------------------------------------ |
| `Task1_DML.sql`                  | Insert, Update and Delete operations |
| `Task2_Single_Table_Queries.sql` | Filtering and sorting queries        |
| `Task3_Multi_Table_Joins.sql`    | Join operations                      |
| `Task4_Aggregations.sql`         | Aggregate functions and grouping     |

### Concepts Covered

* INSERT
* UPDATE
* DELETE
* WHERE clause
* ORDER BY
* GROUP BY
* HAVING
* INNER JOIN
* LEFT JOIN
* Aggregate functions

---

## HandsOn-3 – Advanced SQL Programming

**Technology:** MySQL

This exercise explores advanced SQL features including subqueries, database views, stored procedures, and transaction management.

### Files

| File                                           | Description                        |
| ---------------------------------------------- | ---------------------------------- |
| `Task1_Subqueries.sql`                         | Various subquery examples          |
| `Task2_Views.sql`                              | View creation and usage            |
| `Task3_Stored_Procedures_and_Transactions.sql` | Stored procedures and transactions |

### Concepts Covered

* Nested Queries
* EXISTS / NOT EXISTS
* Views
* WITH CHECK OPTION
* Stored Procedures
* Transactions
* COMMIT
* ROLLBACK
* SAVEPOINT

---

## HandsOn-4 – Query Optimization and Performance

**Technology:** MySQL & Python

Demonstrates techniques for improving SQL query performance using indexes and explains the N+1 Query Problem with a practical Python implementation.

### Files

| File                             | Description               |
| -------------------------------- | ------------------------- |
| `Task1_Baseline_Performance.sql` | Query execution analysis  |
| `Task2_Indexes.sql`              | Index creation            |
| `Task3_N_Plus_One.py`            | N+1 problem demonstration |
| `Task3_Observations.txt`         | Performance comparison    |

### Concepts Covered

* EXPLAIN
* Query execution plans
* Indexing
* Composite indexes
* Query optimization
* N+1 Query Problem
* JOIN optimization

> **Note:** Replace `your_password` with your own MySQL password before executing the Python program.

---

## HandsOn-5 – MongoDB Database Operations

**Technology:** MongoDB

Introduces NoSQL database concepts by creating collections, performing CRUD operations, and working with aggregation pipelines.

### Files

| File                            | Description                         |
| ------------------------------- | ----------------------------------- |
| `Task1_Create_Collection.js`    | Collection creation and sample data |
| `Task2_CRUD_Operations.js`      | CRUD operations                     |
| `Task3_Aggregation_Pipeline.js` | Aggregation examples                |

### Concepts Covered

* Collections
* Documents
* CRUD Operations
* Aggregation Pipeline
* Grouping
* Sorting
* Filtering
* Nested Documents

---

## HandsOn-6 – SQLAlchemy ORM

**Technology:** Python & SQLAlchemy

Introduces Object Relational Mapping (ORM) using SQLAlchemy to perform database operations through Python classes instead of raw SQL.

### Files

| File                     | Description               |
| ------------------------ | ------------------------- |
| `requirements.txt`       | Required Python packages  |
| `Task1_Setup_ORM.py`     | Database connection setup |
| `Task2_CRUD_ORM.py`      | CRUD operations using ORM |
| `Task3_Relationships.py` | Relationship mapping      |

### Concepts Covered

* SQLAlchemy Engine
* Declarative Base
* Sessions
* CRUD Operations
* One-to-Many Relationships
* Foreign Keys
* Relationship Mapping

> **Note:** Update the `DATABASE_URL` with your local database credentials before execution.

---

## HandsOn-7 – Database Version Control with Alembic

**Technology:** Alembic & SQLAlchemy

This exercise demonstrates database schema versioning using Alembic, allowing schema changes to be tracked and applied through migrations.

### Files

| File                           | Description                  |
| ------------------------------ | ---------------------------- |
| `alembic.ini`                  | Alembic configuration        |
| `requirements.txt`             | Required packages            |
| `Task1_Initialize_Alembic.txt` | Alembic initialization       |
| `Task2_Create_Migration.txt`   | Creating migration revisions |
| `Task3_Apply_Migration.txt`    | Applying migrations          |
| `Task4_Rollback_Migration.txt` | Rolling back migrations      |
| `migrations/`                  | Alembic migration files      |

### Frequently Used Commands

```bash
python -m alembic init migrations

python -m alembic revision -m "Initial Migration"

python -m alembic upgrade head

python -m alembic current

python -m alembic downgrade -1

python -m alembic downgrade base

python -m alembic history
```

> **Note:** Configure your database connection inside `alembic.ini` before executing migration commands.

---

# Technologies Used

* Python 3.x
* MySQL
* MongoDB
* SQLAlchemy
* Alembic
* mysql-connector-python
* PyMySQL
* Git
* Visual Studio Code

---

# Prerequisites

Install the required packages using pip:

```bash
pip install mysql-connector-python

pip install sqlalchemy

pip install pymysql

pip install alembic
```

---

# Setup Guide

## MySQL

Execute the SQL scripts in sequence using MySQL Workbench or the MySQL command-line client.

```sql
source HandsOn-1/Task1_Create_Database_and_Tables.sql;

source HandsOn-2/Task1_DML.sql;
```

---

## Python

Install all required libraries before running the ORM and migration exercises.

```bash
pip install mysql-connector-python sqlalchemy pymysql alembic
```

---

## MongoDB

Start MongoDB Shell and execute the following scripts.

```bash
mongosh

load("HandsOn-5/Task1_Create_Collection.js")

load("HandsOn-5/Task2_CRUD_Operations.js")

load("HandsOn-5/Task3_Aggregation_Pipeline.js")
```

---

# Security Best Practices

Database credentials included in the sample programs are represented using the placeholder **your_password**.

For real-world projects, sensitive information should never be stored directly in source code. Instead, use environment variables or configuration files such as `.env`.

Example:

```python
import os

DATABASE_URL = f"mysql+pymysql://root:{os.environ['DB_PASSWORD']}@localhost/college_db"
```

---

# Learning Outcomes

After completing this module, I gained practical experience in:

* Designing normalized relational databases.
* Writing SQL queries for data manipulation and retrieval.
* Working with joins, subqueries, views, and stored procedures.
* Improving database performance through indexing and query optimization.
* Developing NoSQL applications using MongoDB.
* Implementing database operations using SQLAlchemy ORM.
* Managing database schema changes with Alembic migrations.
* Applying industry-standard database development practices.

---

# Acknowledgement

This repository represents the work completed during the **Digital Nurture 5.0 – Python Full Stack Engineer (Python FSE) Deep Skilling Program**. The Database Integration module strengthened my understanding of SQL, NoSQL databases, ORM frameworks, query optimization, and schema migration through practical hands-on exercises.

---

# Author

**RUCHITRA T**

Digital Nurture 5.0 – Python Full Stack Engineer (Python FSE) Deep Skilling Program

**Module:** Database Integration
