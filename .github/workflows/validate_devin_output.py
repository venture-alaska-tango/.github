#!/usr/bin/env python3
"""
Pydantic validation for Devin's GitHub API comment output format.
Ensures structured output enforcement and type safety.
"""

import json
import sys
from typing import List, Literal, Optional
from pydantic import BaseModel, Field, ValidationError


class GitHubComment(BaseModel):
    """Pydantic model for GitHub API review comment structure."""
    body: str = Field(..., description="The review comment text")
    commit_id: str = Field(..., description="SHA of the commit being reviewed")
    path: str = Field(..., description="Relative file path in repo")
    line: int = Field(..., gt=0, description="Line number in PR diff")
    side: Literal["LEFT", "RIGHT"] = Field(..., description="Side of diff")
    start_line: Optional[int] = Field(None, gt=0, description="Start line for multi-line comments")
    start_side: Optional[Literal["LEFT", "RIGHT"]] = Field(None, description="Start side for multi-line comments")
    subject_type: Optional[Literal["line", "file"]] = Field("line", description="Comment target level")


class GitHubReview(BaseModel):
    """Pydantic model for GitHub API review structure."""
    event: Literal["APPROVE", "REQUEST_CHANGES", "COMMENT"] = Field(..., description="Review event type")
    body: str = Field(..., description="Review body text")


def validate_devin_output(output_file: str) -> bool:
    """
    Validate Devin's output against Pydantic models.
    
    Args:
        output_file: Path to JSON file containing Devin's output
        
    Returns:
        bool: True if validation passes, False otherwise
    """
    try:
        with open(output_file, 'r') as f:
            data = json.load(f)
        
        if 'comments' in data:
            for comment in data['comments']:
                GitHubComment(**comment)
                print(f"✅ Valid comment: {comment.get('path', 'unknown')}:{comment.get('line', 'unknown')}")
        
        if 'review' in data:
            GitHubReview(**data['review'])
            print(f"✅ Valid review: {data['review'].get('event', 'unknown')}")
        
        print("🎉 All validations passed!")
        return True
        
    except ValidationError as e:
        print(f"❌ Validation error: {e}")
        return False
    except FileNotFoundError:
        print(f"❌ Output file not found: {output_file}")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_devin_output.py <output_file>")
        sys.exit(1)
    
    success = validate_devin_output(sys.argv[1])
    sys.exit(0 if success else 1)
