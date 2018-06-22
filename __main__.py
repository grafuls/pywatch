import asyncio
import logging


logger = logging.getLogger(__name__)


async def run_local_command(*args):
    process = await asyncio.create_subprocess_exec(
        *args,
        stdout=asyncio.subprocess.PIPE
    )
    logger.info("Started: %s (pid = $s)" % (args, str(process.pid)))

    stdout, stderr = await process.communicate()

    if process.returncode == 0:
        logger.info("Done: %s (pid = %s )" % (args, str(process.pid)))
    else:
        logger.info("Failed: %s (pid = %s )" % (args, str(process.pid)))

    result = stdout.decode().strip()

    return result


if __name__ == "__main__":
    pass
