import gradio as gr


def p(audio):
    return {"text": ""}


def transcribe(audio):
    text = p(audio)["text"]
    return text


gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(source="microphone", type="filepath"),
    outputs="text").launch()
