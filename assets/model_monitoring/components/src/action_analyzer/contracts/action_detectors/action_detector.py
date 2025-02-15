# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""Action Detector Class."""

import pandas
from abc import ABC, abstractmethod
from action_analyzer.contracts.actions.action import Action
from action_analyzer.contracts.llm_client import LLMClient


class ActionDetector(ABC):
    """Action detector base class."""

    def __init__(self,
                 query_intention_enabled: str) -> None:
        """Create an action detector.

        Args:
            query_intention_enabled(str): enable llm generated query intention. Accepted values: true or false.
        """
        self.query_intention_enabled = query_intention_enabled

    @abstractmethod
    def preprocess_data(self, df: pandas.DataFrame) -> pandas.DataFrame:
        """Preprocess the data for action detector.

        Args:
            df(pandas.DataFrame): input pandas dataframe.

        Returns:
            pandas.DataFrame: preprocessed pandas dataframe.
        """
        pass

    @abstractmethod
    def detect(self, df: pandas.DataFrame, llm_client: LLMClient) -> list(Action):
        """Detect the action.

        Args:
            df(pandas.DataFrame): input pandas dataframe.
            llm_client(LLMClient): LLM client used to get some llm scores/info for action.

        Returns:
            list(Action): list of actions.
        """
        pass
