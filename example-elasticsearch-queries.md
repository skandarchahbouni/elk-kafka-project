## 1 - TEXTUAL QUERIES

### Search for activities with a keyword in the description
```json
GET /users-activities/_search
{
  "query": {
    "match": {
      "description": "logged into"
    }
  }
}
```

### Search for all login activities
```json
GET /users-activities/_search
{
  "query": {
    "term": {
      "activity_type": "Login"
    }
  }
}
```

## 2 - AGGREGATION QUERIES

### Average Login Count
```json
GET /users-activities/_search
{
  "size": 0,
  "aggs": {
    "average_login_count": {
      "avg": {
        "field": "login_count"
      }
    }
  }
}
```

### Top N Users by Login Count (Top 5 Users with Highest Login Count):
```json
GET /users-activities/_search
{
  "size": 0, 
  "aggs": {
    "top_users": {
      "terms": {
        "field": "username",  
        "size": 5,
        "order": {
          "total_logins": "desc"   // Sort by total_logins in descending order
        }
      },
      "aggs": {
        "total_logins": {
          "sum": {
            "field": "login_count"
          }
        }
      }
    }
  }
}
```

## 3 - N-GRAM QUERY

### 1. Create a New Index with the N-gram Analyzer
```json
PUT /users-activities-v2
{
  "mappings": {
    "properties": {
      "username": {
        "type": "text",
        "analyzer": "edge_ngram_analyzer"
      }
    }
  },
  "settings": {
    "analysis": {
      "tokenizer": {
        "edge_ngram_tokenizer": {
          "type": "edge_ngram",
          "min_gram": 1,
          "max_gram": 25,
          "token_chars": ["letter", "digit"]
        }
      },
      "analyzer": {
        "edge_ngram_analyzer": {
          "type": "custom",
          "tokenizer": "edge_ngram_tokenizer"
        }
      }
    }
  }
}
```

### 2. Reindex Data from the Old Index to the New Index
```json
POST /_reindex
{
  "source": {
    "index": "users-activities"  // Old index name
  },
  "dest": {
    "index": "users-activities-v2"  // New index name
  }
}
```

### 3. Search Query Example
```json
GET /users-activities-v2/_search
{
  "query": {
    "match": {
      "username": {
        "query": "bgr",  // User types "bgr"
        "operator": "and"
      }
    }
  }
}
```
In this setup, the username field will be tokenized into n-grams, allowing for partial matching (e.g., typing "bgr" could match "bgraveston0").

## 4 - FUZZY QUERIES

### Query Example (Fuzziness = 1)
```json
GET /users-activities/_search
{
  "query": {
    "fuzzy": {
      "username": {
        "value": "nvanz2",  // Slight typo (missing 'z')
        "fuzziness": 1         // Allow 1 character modification
      }
    }
  }
}
```

### Query Example (Fuzziness = 2)
```json
GET /users-activities/_search
{
  "query": {
    "fuzzy": {
      "username": {
        "value": "mvanz2",  
        "fuzziness": 2        // Allow 2 character modification
      }
    }
  }
}
```

## 5 - Time series
### Date Histogram Aggregation
```json
GET /users-activities/_search
{
  "size": 0,  // We are only interested in aggregations, not actual hits
  "aggs": {
    "activities_over_time": {
      "date_histogram": {
        "field": "timestamp",         // The field to aggregate on,
        "fixed_interval": "1d",            // Time interval for aggregation
        "format": "yyyy-MM-dd"        // Optional: Formatting the date in the response
      }
    }
  }
}
```
