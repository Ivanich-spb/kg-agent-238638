"""Basic example showing how to instantiate and run the KG-Agent.

Run: python -m examples.basic
"""
from framework_name import KGAgent, KGExecutor, Memory, Toolbox


def dummy_llm(prompt, metadata=None):
    """Very small deterministic LLM stub used for the example.

    Args:
        prompt: Prompt string.
        metadata: Optional metadata dict.
    Returns:
        A small action string interpreted by the agent.
    """
    # This hard-coded behavior demonstrates the agent loop
    if 'retrieve' in prompt.lower():
        return 'CALL retrieve_facts actor:Tom_Hanks'
    return 'ANSWER: Demo answer produced by dummy LLM.'


def retrieve_facts_stub(args):
    """Simple tool that pretends to retrieve facts from a KG or search index.

    Args:
        args: Raw argument string provided by the LLM.
    Returns:
        A dict with retrieved facts.
    """
    # TODO: Replace with a real retriever that queries a KG
    return {'query': args, 'facts': ['Tom Hanks -> actor', 'Tom Hanks -> born_in Concord']}


def main():
    # Initialize components
    executor = KGExecutor()
    memory = Memory()
    toolbox = Toolbox()
    toolbox.register('retrieve_facts', retrieve_facts_stub)

    agent = KGAgent(llm=dummy_llm, executor=executor, toolbox=toolbox, memory=memory)

    question = 'Who is the actor that starred in the movie Forrest Gump?'
    answer = agent.run(question)
    print('Final answer:', answer)

    # Inspect memory
    print('\nMemory contents:')
    for item in memory.query():
        print(item)


if __name__ == '__main__':
    main()
