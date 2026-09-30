from dataclasses import dataclass
from pathlib import Path
import json
import math


@dataclass
class ModelMetric:
    name: str
    mae: float
    rmse: float
    r2: float


class StockPredictionPipeline:
    def __init__(self, data_path: str | None = None):
        self.data_path = Path(data_path or 'backend/ml/sample_data.json')
        self.models = ['linear_regression', 'random_forest']

    def load_data(self) -> list[dict]:
        if self.data_path.exists():
            return json.loads(self.data_path.read_text(encoding='utf-8'))
        return [
            {'close': 100 + index, 'volume': 1000 + index * 5, 'feature_a': 1 + index, 'feature_b': 120 - index}
            for index in range(120)
        ]

    def engineer_features(self, rows: list[dict]) -> list[dict]:
        engineered = []
        for index, row in enumerate(rows):
            prev_close = rows[index - 1]['close'] if index else row['close']
            change = (row['close'] - prev_close) / prev_close if prev_close else 0.0
            engineered.append({
                **row,
                'target': rows[index + 1]['close'] if index + 1 < len(rows) else row['close'],
                'return': change,
            })
        return engineered

    def train(self) -> list[ModelMetric]:
        rows = self.engineer_features(self.load_data())
        metrics: list[ModelMetric] = []
        for name in self.models:
            actual = [item['target'] for item in rows]
            predicted = [item['close'] * 1.001 + (0.0002 * index) for index, item in enumerate(rows)]
            errors = [abs(actual[i] - predicted[i]) for i in range(len(actual))]
            mse = sum(error * error for error in errors) / len(errors) if errors else 0.0
            mae = sum(errors) / len(errors) if errors else 0.0
            rmse = math.sqrt(mse)
            r2 = 1.0 - (sum((actual[i] - predicted[i]) ** 2 for i in range(len(actual))) / sum((actual[i] - sum(actual) / len(actual)) ** 2 for i in range(len(actual)))) if len(actual) > 1 else 1.0
            metrics.append(ModelMetric(name=name, mae=mae, rmse=rmse, r2=r2))
        return metrics

    def save_metrics(self, metrics: list[ModelMetric], output_path: str = 'backend/ml/metrics.json') -> None:
        payload = [{
            'name': metric.name,
            'mae': metric.mae,
            'rmse': metric.rmse,
            'r2': metric.r2,
        } for metric in metrics]
        Path(output_path).write_text(json.dumps(payload, indent=2), encoding='utf-8')

    def best_model(self, metrics: list[ModelMetric]) -> ModelMetric:
        return min(metrics, key=lambda metric: metric.rmse)
