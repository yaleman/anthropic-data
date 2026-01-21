from uuid import UUID
from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel, RootModel, ConfigDict, Field, field_validator


from .loader import Loader
from .account import Account


class ChatFile(BaseModel):
    file_name: str

    model_config = ConfigDict(extra="forbid")


class ChatMessageSummary(BaseModel):
    summary: str
    model_config = ConfigDict(extra="forbid")


class Attachment(BaseModel):
    file_name: str
    extracted_content: str
    file_type: str
    file_size: int

    model_config = ConfigDict(extra="forbid")


class CitationDetails(BaseModel):
    citation_type: str = Field(..., alias="type")
    url: str
    model_config = ConfigDict(extra="forbid")


class Citation(BaseModel):
    uuid: UUID
    title: Optional[str] = Field(None)
    url: Optional[str] = Field(None)
    origin_tool_name: Optional[str] = Field(None)
    metadata: dict[str, Any] = Field(default_factory=dict)
    details: Optional[CitationDetails] = Field(None)
    start_index: int
    end_index: int
    sources: list[dict[str, Any]] = Field(default_factory=list)
    model_config = ConfigDict(extra="forbid")


class ChatInput(BaseModel):
    id: Optional[str] = Field(None)
    version_uuid: Optional[UUID] = Field(None)
    language: Optional[str] = Field(None)
    url: Optional[str] = Field(None)
    n: Optional[int] = Field(None)
    old_str: Optional[str] = Field(None)
    new_str: Optional[str] = Field(None)
    code: Optional[str] = Field(None)
    query: Optional[str] = Field(None)
    md_citations: list[Citation] = Field(default_factory=list)
    content: Optional[str] = Field(None)
    command: Optional[str] = Field(None)
    source: Optional[str] = Field(None)
    title: Optional[str] = Field(None)
    type: Optional[str] = Field(None)
    model_config = ConfigDict(extra="forbid")


class ChatMessageContent(BaseModel):
    id: Optional[UUID] = Field(None)
    name: Optional[str] = Field(None)
    input: Optional[ChatInput] = Field(None)
    approval_key: Optional[str] = Field(None)
    approval_options: Optional[str] = Field(None)
    start_timestamp: Optional[datetime] = Field(None)
    stop_timestamp: Optional[datetime] = Field(None)
    display_content: Optional[dict[str, Any]] = Field(None)
    context: Optional[str] = Field(None)
    content: Optional[Any] = Field(None)
    typename: str = Field(
        ...,
        alias="type",
    )
    alternative_display_type: Optional[str] = Field(None)
    cut_off: Optional[bool] = Field(None)
    citations: list[Citation] = Field(default_factory=list)
    text: Optional[str] = Field(None)
    flags: Optional[str]
    thinking: Optional[str] = Field(None)
    summaries: list[ChatMessageSummary] = Field(default_factory=list)
    integration_name: Optional[str] = Field(None)
    integration_icon_url: Optional[str] = Field(None)
    message: Optional[str] = Field(None)
    structured_content: Optional[dict[str, Any]] = Field(None)
    is_error: bool = Field(False)
    meta: Optional[str] = Field(None)
    tool_use_id: Optional[UUID] = Field(None)

    model_config = ConfigDict(extra="forbid")

    @field_validator("typename")
    def validate_typename(cls, v: str) -> str:
        allowed_types = {
            "thinking",
            "text",
            "code",
            "image",
            "video",
            "audio",
            "file",
            "knowledge",
        }
        if v not in allowed_types:
            raise ValueError(f"type must be one of {allowed_types}")
        return v


class ChatMessage(BaseModel):
    uuid: UUID
    files: list[ChatFile]
    attachments: list[Attachment] = Field(default_factory=list)
    created_at: datetime
    updated_at: datetime
    content: list[ChatMessageContent] = Field(default_factory=list)
    text: str
    sender: str
    model_config = ConfigDict(extra="forbid")

    @field_validator("sender")
    def validate_sender(cls, v: str) -> str:
        allowed_senders = {"human", "assistant"}
        if v not in allowed_senders:
            raise ValueError(f"sender must be one of {allowed_senders}")
        return v


class Conversation(BaseModel):
    uuid: UUID
    name: str
    summary: str

    account: Account
    created_at: datetime
    updated_at: datetime
    chat_messages: list[ChatMessage]

    model_config = ConfigDict(extra="forbid")


class Conversations(RootModel[list[Conversation]], Loader):
    root: list[Conversation]


if __name__ == "__main__":
    conversations = Conversations.load("conversations.json")
    print(
        conversations.model_dump_json(
            indent=2, by_alias=True, exclude_none=True, exclude_unset=True
        )
    )
