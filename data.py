from numerapi import NumerAPI
api = NumerAPI()
api.download_dataset(
	"v5.0/train.parquet",
	"train.parquet"
)
api.download_dataset(
	"v5.0/validation.parquet",
	"validation.parquet"
)
api.download_dataset(
	"v5.0/validation_example_preds.parquet",
	"validation_example_preds.parquet"
)
api.download_dataset(
	"v5.0/live.parquet",
	"live.parquet"
)
api.download_dataset(
	"v5.0/live_example_preds.parquet",
	"live_example_preds.parquet"
)
api.download_dataset(
	"v5.0/features.json",
	"features.json"
)
api.download_dataset(
	"v5.0/train_benchmark_models.parquet",
	"train_benchmark_models.parquet"
)
api.download_dataset(
	"v5.0/validation_benchmark_models.parquet",
	"validation_benchmark_models.parquet"
)
api.download_dataset(
	"v5.0/live_benchmark_models.parquet",
	"live_benchmark_models.parquet"
)
api.download_dataset(
	"v5.0/meta_model.parquet",
	"meta_model.parquet"
)

