from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

# Load model and tokenizer once (on app start)
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def summarize_text(text, max_input_length=512, max_output_length=150):
    # Prepend the T5 task prefix
    input_text = "summarize: " + text.strip().replace("\n", " ")

    # Tokenize input (truncate to max_input_length)
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=max_input_length, truncation=True)

    # Generate summary ids
    summary_ids = model.generate(inputs, max_length=max_output_length, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)

    # Decode summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary
