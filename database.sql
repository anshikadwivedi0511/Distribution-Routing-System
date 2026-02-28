CREATE DATABASE distributionsystem;
USE distributionsystem;

CREATE TABLE nodes (
  node_id int NOT NULL AUTO_INCREMENT,
  name varchar(100) DEFAULT NULL,
  latitude decimal(9,6) DEFAULT NULL,
  longitude decimal(9,6) DEFAULT NULL,
  node_type varchar(20) DEFAULT NULL,
  PRIMARY KEY (node_id)
);

CREATE TABLE routes (
  route_id int NOT NULL AUTO_INCREMENT,
  source_node_id int NOT NULL,
  destination_node_id int NOT NULL,
 distance_km decimal(10,4) DEFAULT NULL,
  road_type varchar(50) DEFAULT 'Main Road',
  fuel_cost decimal(10,2) DEFAULT NULL,
  traffic_factor int DEFAULT 0 ,
  weather_factor int DEFAULT 0,
  final_cost decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (route_id),
  KEY source_node_id (source_node_id),
  KEY destination_node_id (destination_node_id),

   CONSTRAINT routes_ibfk_1 FOREIGN KEY (source_node_id) REFERENCES nodes (node_id),
  CONSTRAINT routes_ibfk_2 FOREIGN KEY (destination_node_id) REFERENCES nodes (node_id)
);