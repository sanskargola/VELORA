CREATE DATABASE IF NOT EXISTS stockvision;
USE stockvision;

CREATE TABLE users (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role ENUM('admin','user') DEFAULT 'user',
  is_verified TINYINT(1) DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_users_email (email)
);

CREATE TABLE user_profiles (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  full_name VARCHAR(255),
  timezone VARCHAR(64),
  avatar_url VARCHAR(500),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE stocks (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  symbol VARCHAR(16) UNIQUE NOT NULL,
  company_name VARCHAR(255) NOT NULL,
  sector VARCHAR(128),
  market_cap BIGINT,
  currency VARCHAR(8) DEFAULT 'USD',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_stocks_symbol (symbol)
);

CREATE TABLE historical_prices (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  stock_id BIGINT NOT NULL,
  date DATE NOT NULL,
  open_price DECIMAL(12,4),
  high_price DECIMAL(12,4),
  low_price DECIMAL(12,4),
  close_price DECIMAL(12,4),
  volume BIGINT,
  FOREIGN KEY (stock_id) REFERENCES stocks(id) ON DELETE CASCADE,
  UNIQUE KEY uq_hist (stock_id, date)
);

CREATE TABLE live_prices (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  stock_id BIGINT NOT NULL,
  price DECIMAL(12,4) NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (stock_id) REFERENCES stocks(id) ON DELETE CASCADE
);

CREATE TABLE technical_indicators (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  stock_id BIGINT NOT NULL,
  date DATE NOT NULL,
  sma_20 DECIMAL(12,4),
  ema_20 DECIMAL(12,4),
  rsi DECIMAL(8,4),
  macd DECIMAL(12,4),
  atr DECIMAL(12,4),
  vwap DECIMAL(12,4),
  FOREIGN KEY (stock_id) REFERENCES stocks(id) ON DELETE CASCADE,
  UNIQUE KEY uq_indicators (stock_id, date)
);

CREATE TABLE ml_models (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  type VARCHAR(100) NOT NULL,
  version VARCHAR(50),
  accuracy DECIMAL(6,4),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE predictions (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  user_id BIGINT,
  stock_id BIGINT NOT NULL,
  model_id BIGINT,
  predicted_price DECIMAL(12,4) NOT NULL,
  confidence_score DECIMAL(6,4),
  recommendation VARCHAR(16),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL,
  FOREIGN KEY (stock_id) REFERENCES stocks(id) ON DELETE CASCADE,
  FOREIGN KEY (model_id) REFERENCES ml_models(id) ON DELETE SET NULL,
  INDEX idx_predictions_stock (stock_id, created_at)
);

CREATE TABLE prediction_history (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  prediction_id BIGINT NOT NULL,
  actual_price DECIMAL(12,4),
  error DECIMAL(12,4),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (prediction_id) REFERENCES predictions(id) ON DELETE CASCADE
);

CREATE TABLE model_performance (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  model_id BIGINT NOT NULL,
  mae DECIMAL(10,4),
  rmse DECIMAL(10,4),
  mape DECIMAL(10,4),
  r2_score DECIMAL(10,4),
  recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (model_id) REFERENCES ml_models(id) ON DELETE CASCADE
);

CREATE TABLE news_articles (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  source VARCHAR(100),
  url VARCHAR(500),
  published_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE sentiment_analysis (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  news_id BIGINT NOT NULL,
  positive_pct DECIMAL(5,2),
  neutral_pct DECIMAL(5,2),
  negative_pct DECIMAL(5,2),
  overall_mood VARCHAR(32),
  FOREIGN KEY (news_id) REFERENCES news_articles(id) ON DELETE CASCADE
);

CREATE TABLE watchlists (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  name VARCHAR(100) DEFAULT 'My Watchlist',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE portfolio (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  stock_id BIGINT NOT NULL,
  quantity DECIMAL(12,4) NOT NULL,
  avg_buy_price DECIMAL(12,4) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (stock_id) REFERENCES stocks(id) ON DELETE CASCADE
);

CREATE TABLE transactions (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  stock_id BIGINT NOT NULL,
  type ENUM('buy','sell') NOT NULL,
  quantity DECIMAL(12,4) NOT NULL,
  price DECIMAL(12,4) NOT NULL,
  executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (stock_id) REFERENCES stocks(id) ON DELETE CASCADE
);

CREATE TABLE alerts (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  stock_id BIGINT NOT NULL,
  threshold DECIMAL(12,4),
  alert_type VARCHAR(32),
  is_active TINYINT(1) DEFAULT 1,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (stock_id) REFERENCES stocks(id) ON DELETE CASCADE
);

CREATE TABLE notifications (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  message VARCHAR(255) NOT NULL,
  is_read TINYINT(1) DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE activity_logs (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  user_id BIGINT,
  action VARCHAR(255) NOT NULL,
  details JSON,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
);

CREATE TABLE api_usage (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  endpoint VARCHAR(255),
  request_count BIGINT DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE settings (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  user_id BIGINT NOT NULL,
  theme VARCHAR(16) DEFAULT 'dark',
  notifications_enabled TINYINT(1) DEFAULT 1,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE feedback (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  user_id BIGINT,
  message TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
);

CREATE VIEW vw_dashboard_summary AS
SELECT
  (SELECT COUNT(*) FROM users) AS total_users,
  (SELECT COUNT(*) FROM predictions) AS total_predictions,
  (SELECT COUNT(*) FROM news_articles) AS total_news;

DELIMITER $$
CREATE PROCEDURE sp_get_top_stocks()
BEGIN
  SELECT symbol, company_name FROM stocks ORDER BY id LIMIT 10;
END$$
DELIMITER ;
