import chainlit as cl
from graph import graph

@cl.on_message
async def handle_message(message: cl.Message):
    user_query = message.content

    # Show steps to user
    async with cl.Step(name="🧠 Planner - Creating research plan..."):
        pass

    async with cl.Step(name="🔍 Researchers - Searching the web in parallel..."):
        pass

    async with cl.Step(name="✍️ Synthesizer - Writing final answer..."):
        result = await cl.make_async(graph.invoke)({"query": user_query})

    # Send final answer
    await cl.Message(content=result["final_answer"]).send()