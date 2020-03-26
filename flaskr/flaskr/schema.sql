DROP TABLE IF EXISTS devjegan.user;
DROP TABLE IF EXISTS devjegan.post;

CREATE TABLE devjegan.user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE devjegan.post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE devjegan.user (                                        
  id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY (START WITH 1 
                         INCREMENT BY 1) ,                          
  username varchar(30) UNIQUE NOT NULL,                             
  password varchar(128) NOT NULL                                     
)                                                                   

CREATE TABLE devjegan.post (                                        
  id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY (START WITH 1 
                         INCREMENT BY 1) ,                          
  author_id INTEGER NOT NULL,                                       
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,             
  title varchar(100) NOT NULL,                                      
  body varchar(1000) NOT NULL,                                      
  FOREIGN KEY (author_id) REFERENCES devjegan.user (id)             
)                                                                   