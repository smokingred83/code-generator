from pathlib import Path
from pipelines import data_etl
import click


@click.command(
    help="""
Code generator project CLI v0.0.1. 
Main entry point for the pipeline execution.
"""
)
@click.option(
    "--no-cache",
    is_flag=True,
    default=False,
    help="Disable caching for the pipeline run.",
)
@click.option(
    "--run-etl",
    is_flag=True,
    default=False,
    help="Whether to run the ETL pipeline.",
)
@click.option(
    "--etl-config-filename",
    default="digital_data_etl_paul_iusztin.yaml",
    help="Filename of the ETL config file.",
)

def main(
    no_cache: bool = False,
    run_etl: bool = False,
    etl_config_filename: str = "data_etl_gg.yaml"
) -> None:
    assert (
        run_etl
    ), "Please specify an action to run."

    pipeline_args = {
        "enable_cache": not no_cache,
    }
    root_dir = Path(__file__).resolve().parent.parent

    if run_etl:
        run_args_etl = {}
        pipeline_args["config_path"] = root_dir / "configs" / etl_config_filename
        assert pipeline_args["config_path"].exists(), f"Config file not found: {pipeline_args['config_path']}"
        pipeline_args["run_name"] = f"data_etl_run_{dt.now().strftime('%Y_%m_%d_%H_%M_%S')}"
        data_etl.with_options(**pipeline_args)(**run_args_etl)

if __name__ == "__main__":
    main()